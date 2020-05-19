from django.shortcuts import render
from projects.models import Project

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
