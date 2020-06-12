from django.shortcuts import render
from projects.models import Project

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

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
