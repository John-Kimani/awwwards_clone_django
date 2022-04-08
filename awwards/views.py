from django.shortcuts import render


def homepage(request):
    '''
    View function that renders homepage
    '''

    return render(request, 'awwards/homepage.html')
