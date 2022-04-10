from django.shortcuts import render
from .forms import ProjectSubmissionForm


def homepage(request):
    '''
    View function that renders homepage
    '''

    return render(request, 'awwards/homepage.html')


def publish_project(request):
    '''
    View function that render postproject page
    '''
    form = ProjectSubmissionForm()

    return render(request, 'awwards/submitproject.html', {"form":form})
