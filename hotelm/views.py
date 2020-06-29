from django.http import HttpResponseRedirect, JsonResponse
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.mail import EmailMultiAlternatives, send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django_apscheduler.jobstores import DjangoJob, register_job
from apscheduler.schedulers.background import BackgroundScheduler
import datetime, time, pytz

from .models import Search
from .forms import SearchForm, SignUpForm, CommentForm
from .marriott import email_marriott_results, fill_form, prepare_driver, scrape_results, driver_test
from .jobs import search_and_email
from challenge.settings import EMAIL_HOST_USER

# Homepage
def hotel_index(request):
    return render(request, 'hotelm/index.html')

# About page
def about(request):
    time = datetime.datetime.now()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_email = form.cleaned_data['email']
            comment_subject = form.cleaned_data['subject']
            comment_body = form.cleaned_data['comment']
            msg = EmailMultiAlternatives(
                subject = comment_subject,
                body = comment_body,
                from_email = 'csprojects200220@gmail.com',
                to = ['jedhcl@gmail.com'],
            )
            msg.send()
            message = 'Message sent to the moderator!'
            return render(request, 'hotelm/about.html', {'time': time, 'form': form, 'message': message})
    # initial form screen
    else:
        form = CommentForm()
    return render(request, 'hotelm/about.html', {'time': time,'form': form})

# logout user page
def logout_request(request):
    logout(request)
    message = 'Logout successful.'
    return render(request, 'hotelm/search.html', {'message': message})

# login user page
def login_request(request):
    message = ''
    # if request.user.is_authenticated():
    #     return render(request, 'hotelm/index.html')
    if request.user.is_authenticated:
        message = 'You are already logged in as: ', request.user.username
        return render(request, 'hotelm/search.html', {'message': message})
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            message = 'Login successful!'
            return render(request, 'hotelm/search.html', {'message': message})
        else:
            form = AuthenticationForm()
            message = 'Invalid username or password.'
            return render(request, "auth/login.html", {"form": form, "message": message})
    else:
        form = AuthenticationForm()
        return render(request, "auth/login.html", {"form": form, "message": message})

# register user page
def register(request):
    if request.user.is_authenticated:
        return redirect('/', message = 'Already registered')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'hotelm/search.html', {'message': 'Registered!'})
        else:
            form = SignUpForm()
            return render(request, 'auth/register.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'auth/register.html', {'form': form})

# Search page
def get_search(request):
    # If form is filled:
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # Create Search object
            if form.cleaned_data['special_rates']:
                sp = form.cleaned_data['special_rates']
            else:
                sp = "0"
            if form.cleaned_data['special_rates_code']:
                spc = form.cleaned_data['special_rates_code']
            else:
                spc = "0"
            local = pytz.timezone("America/Los_Angeles")
            searchobj = Search(
                recipient = form.cleaned_data['email'],
                destination = form.cleaned_data['destination'],
                check_in = form.cleaned_data['cin_date'],
                check_out = form.cleaned_data['cout_date'],
                special_rates = sp,
                special_rates_code = spc
            )
            if request.user.is_authenticated:
                searchobj.user = request.user
            if form.cleaned_data['email_freq']:
                searchobj.recurrence = int(form.cleaned_data['email_freq']) + 1
            else:
                searchobj.recurrence = 1
            searchobj.save()
            #search and email results
            searchobj_id=str(int(searchobj.id))
            #create recurrence object
            scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)
            scheduler.add_job(search_and_email, 'interval', seconds = 86400, id=searchobj_id, max_instances = 3, coalesce = True, next_run_time=datetime.datetime.now(), args=[searchobj_id])
            register_job(scheduler)
            scheduler.start()
            message = 'Search Results will be sent to your email. Please check your email in about 60 seconds. Thank you.'
            return render(request, 'hotelm/search.html', {'message': message})
    # initial form screen
    else:
        form = SearchForm()
    return render(request, 'hotelm/search.html', {'form': form})

def history(request):
    items = Search.objects.all().filter(user=request.user)
    return render(request, 'hotelm/history.html', {'items': items})

def delete_search(request):
    if request.method == 'POST':
        search_id = int(request.POST.get('search_id'))
        search_obj = Search.objects.get(pk=search_id)
        search_obj.delete()
        search_id_str = str(search_id)
        try:
            DjangoJob.objects.get(name=search_id_str).delete()
            print("DjangoJob deleted. ID=",search_id)
        except:
            next
        items = Search.objects.all().filter(user=request.user)
        return render(request, 'hotelm/history.html', {'items': items})

def print_delay():
    print('print_delay test')

def email_test():
    print('email_test start')
    res = [['1','1','1','1'],['2','2','2','2'],['3','3','3','3']]
    subject = 'Email-test'
    txt_message = 'Have a great day!'
    html_body = render_to_string('hotelm/results_email.html', {'res': res})
    msg = EmailMultiAlternatives(
        subject = subject,
        body = txt_message,
        from_email = 'csprojects200220@gmail.com',
        to = ['jedhcl@gmail.com'],
    )
    msg.attach_alternative(html_body, "text/html")
    time.sleep(60)
    msg.send()
    print('email_test message sent')

def test(request):
    driver_test()
    # scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)
    # scheduler.add_job(print_delay, 'interval', seconds = 15, max_instances = 3, coalesce = True, next_run_time=datetime.datetime.now())
    # register_job(scheduler)
    # scheduler.start()
    return render(request, 'hotelm/search.html')
