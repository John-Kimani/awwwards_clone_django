from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 

def register(request):
    '''
    User registration view
    '''
    form = UserCreationForm()
    return render(request, 'members/register.html', {"form":form})
