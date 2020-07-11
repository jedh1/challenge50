from django.shortcuts import render, redirect
from projects.models import Project

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# For xy_plotter
from django.contrib import messages
from plotly.offline import plot
from plotly.graph_objs import Scatter
import pandas as pd
# For backtesting
from pandas_datareader import data as pdr
from django.contrib import messages
from django.http import HttpResponse
from bokeh.plotting import figure, output_file, show, ColumnDataSource
import bokeh.layouts
from bokeh.embed import components
from bokeh.models import HoverTool
from datetime import date
from .forms import sma_search
from .btsingle import btsingle

# Create your views here.
def index(request):
    return render(request, 'index.html')

def project_index(request):
    projects = Project.objects.all()
    projects = projects.order_by('pk').reverse()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

def about(request):
    return render(request, 'about.html')

def sample(request):
    subject = 'Challenge email test'
    txt_message = 'Have a great day!'
    html_body = render_to_string('about.html')
    msg = EmailMultiAlternatives(
        subject = subject,
        body = txt_message,
        from_email = 'csprojects200220@gmail.com',
        to = ['jedhcl@gmail.com'],
    )
    msg.attach_alternative(html_body, "text/html")
    msg.send()
    return render(request, 'sample.html')
#
# Projects for 30projects30days
# https://plotly.com/python/line-and-scatter/
# XY Plotter
def xy_plotter(request):
    intro = True
    if request.method == 'GET':
        df = { "X":[-4, -3, -2, -1, 0,1,2,3,4,2,-2,-2,2,3,-3,3], "Y": [-4,5,3,-4,2,3,-3,4,-1,2,2,-2,-2,3,3,-3], "Z": [-3,2,5,3,-2,-4,5,2,1,2,4,3,0,-1,-2,-3]}
        plot_div = plot([Scatter(
                        x = df['X'],
                        y = df['Y'],
                        mode='markers',
                        name='test',
                        marker_color=df['Z'],
                        marker_colorscale=['red','yellow','green'],
                        text=df['Z'],
                        )],
                    output_type='div')
        return render(request, "xy_plotter.html", context={'plot_div': plot_div})
    if request.method == 'POST':
        test_file = request.FILES['testFile']
        if test_file:
            # Check if file is csv
            if not test_file.name.endswith('.csv'):
                messages.error(request,'Error: File is not CSV type')
            # if file is too large, return message
            if test_file.multiple_chunks():
                messages.error(request,"Error: Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
            # read file
            colnames = ['X', 'Y', 'Z']
            df = pd.read_csv(test_file, names=colnames, header=None)
            plot_div = plot([Scatter(
                            x = df['X'],
                            y = df['Y'],
                            mode='markers',
                            name='test',
                            marker_color=df['Z'],
                            marker_colorscale=['red','yellow','green'],
                            text=df['Z'],
                            )],
                        output_type='div')
            intro = False
        else:
            plot_div = 'fail'
            messages.warning(request, f'No file to process! Please upload a file to process.')
    return render(request, "xy_plotter.html", context={'plot_div': plot_div})

# Backtesting SMA
def btindex(request):
    # If form is filled:
    if request.method == 'POST':
        form = sma_search(request.POST)
        if form.is_valid():
            # Create Search object
            stock_in = form.cleaned_data.get('ticker')
            start_date_in = form.cleaned_data.get('start_date')
            end_date_in = form.cleaned_data.get('end_date')
            pfast = form.cleaned_data.get('sma_fast')
            pslow = form.cleaned_data.get('sma_slow')
            error_count = 0

            #check form is valid:
            if start_date_in >= end_date_in:
                messages.error(request, 'Form error: End date must be later than start date,')
                error_count += 1

            if pfast >= pslow:
                messages.error(request, 'Form error: SMA, fast must be less than SMA, slow.')
                error_count += 1

            if error_count > 0:
                error_count = 0
                return redirect('btindex')

            try:
                script, div, sr = btsingle(stock_in, start_date_in, end_date_in, pfast, pslow)
            except:
                messages.error(request, 'Form error')
                return redirect('btindex')

            return render(request,'btresults.html', {'script':script, 'div':div, 'sr':sr, 'ticker': stock_in.upper(), 'fsma': pfast, 'ssma': pslow, 'start':start_date_in, 'end':end_date_in})
    # initial form screen
    else:
        form = sma_search()
    return render(request, 'btindex.html', {'form': form})

def bt_ex1(request):
    #input variables
    stock_in = 'TSLA'
    start_date_in = '2016-01-01'
    end_date_in = '2017-12-25'
    pfast = 7
    pslow = 66
    #run strategy
    script, div, sharpe_ratio = btsingle(stock_in, start_date_in, end_date_in, pfast, pslow)
    return render(request,'btresults.html', {'script':script, 'div':div, 'sr':sharpe_ratio, 'ticker': stock_in, 'fsma': pfast, 'ssma': pslow, 'start':start_date_in, 'end':end_date_in})

def bt_ex2(request):
    #input variables
    stock_in = 'SPY'
    start_date_in = '2016-01-01'
    end_date_in = '2019-12-25'
    pfast = 50
    pslow = 200
    #run strategy
    script, div, sharpe_ratio = btsingle(stock_in, start_date_in, end_date_in, pfast, pslow)
    return render(request,'btresults.html', {'script':script, 'div':div, 'sr':sharpe_ratio, 'ticker': stock_in, 'fsma': pfast, 'ssma': pslow, 'start':start_date_in, 'end':end_date_in})

# Other projects (JS based)
def clockview(request):
    return render(request, 'clockview.html')

def validator(request):
    return render(request, 'validator.html')

def movie(request):
    return render(request, 'movie.html')

def video(request):
    return render(request, 'video.html')

def exchange_rate(request):
    return render(request, 'exchange_rate.html')

def dom_array(request):
    return render(request, 'dom_array.html')

def landing_page(request):
    return render(request, 'landing_page.html')

def hangman(request):
    return render(request, 'hangman.html')

def calculator(request):
    return render(request, 'calculator.html')

def scrambled_words(request):
    return render(request, 'scrambled_words.html')

def cookies_demo(request):
    return render(request, 'cookies_demo.html')

def create_csv(request):
    return render(request, 'create_csv.html')

def drag_drop(request):
    return render(request, 'drag_drop.html')

def post_scrolling(request):
    return render(request, 'post_scrolling.html')

def flash_cards(request):
    return render(request, 'flash_cards.html')

def lyrics_search(request):
    return render(request, 'lyrics_search.html')

def breakout(request):
    return render(request, 'breakout.html')

def relaxer(request):
    return render(request, 'relaxer.html')

def new_year_countdown(request):
    return render(request, 'new_year_countdown.html')

def speech_reader(request):
    return render(request, 'speech_reader.html')

def speak_number(request):
    return render(request, 'speak_number.html')

def car_driving_game(request):
    return render(request, 'car_driving_game.html')

def expense_tracker(request):
    return render(request, 'expense_tracker.html')

def music_player(request):
    return render(request, 'music_player.html')

def typing_game(request):
    return render(request, 'typing_game.html')

def meal_finder(request):
    return render(request, 'meal_finder.html')

def hi_lo(request):
    return render(request, 'hi_lo.html')

def floppy_bird(request):
    return render(request, 'floppy_bird.html')
