from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MemberRegisterForm

def register(request):
    '''
    User registration view
    '''
    if request.method == 'POST':
        form = MemberRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created {username}')
            return redirect('homepage')
    else:
        form = MemberRegisterForm()
    return render(request, 'members/register.html', {"form":form})
