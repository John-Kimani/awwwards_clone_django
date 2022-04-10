from django.shortcuts import render,redirect
from .forms import ProjectSubmissionForm,UpdateProjectForm
from .models import Projects
from django.contrib import messages


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
    if request.method == 'POST':
        form = ProjectSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            project= Projects()
            project.user = form.cleaned_data['user']
            project.title = form.cleaned_data['title']
            project.article = form.cleaned_data['article']
            project.link = form.cleaned_data['link']
            project.image = form.cleaned_data['image']
            project.save()
            messages.success(request, f'Your project has been submitted')
            return redirect('homepage')
    else:
        form = ProjectSubmissionForm()

    return render(request, 'awwards/submitproject.html', {"form":form})

def update_project(request):
    '''
    View function that render project update from
    '''
    form = UpdateProjectForm()
    return render(request, 'awwards/project.html',{"form":form})

def view_project(request, project_id):
    '''
    View function that render project on one page 
    '''
    project = Projects.objects.get(pk = project_id)
    return render(request, 'awwards/singleproject.html',{"projects":project})