from django.shortcuts import render


def homepage(request):
    '''
    View function that renders homepage
    '''

    return render(request, 'awwards/homepage.html')


def publish_project(request):
    '''
    View function that render postproject page
    '''

    return render(request, 'awwards/submitproject.html')
