from django.shortcuts import render
from projects.models import Project

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# For xy_plotter
from django.contrib import messages
from plotly.offline import plot
from plotly.graph_objs import Scatter
import pandas as pd

# Create your views here.
def project_index(request):
    projects = Project.objects.all()
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
# Create your views here.
# https://plotly.com/python/line-and-scatter/
def xy_plotter(request):
    intro = True
    if request.method == 'GET':
        df = { "X":[-4, -3, -2, -1, 0], "Y": [-4, -3, -2, -1, 0], "Z": [1, 2, 4, -3]}
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
