from django.shortcuts import render
from .forms import ProjectSubmissionForm
from .models import Projects


def homepage(request):
    '''
    View function that renders homepage
    '''
    projects = Projects.objects.all()

    return render(request, 'awwards/homepage.html', {"projects": projects})


def publish_project(request):
    '''
    View function that render postproject page
    '''
    form = ProjectSubmissionForm()

    return render(request, 'awwards/submitproject.html', {"form":form})

def update_project(request):
    '''
    View function that render project update from
    '''
    return render(request, 'awwards/project.html')