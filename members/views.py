from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MemberRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile

def register(request):
    '''
    User registration view
    '''
    if request.method == 'POST':
        form = MemberRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You can now login')
            return redirect('login')
    else:
        form = MemberRegisterForm()
    return render(request, 'members/register.html', {"form":form})

@login_required()
def member_profile(request):
    '''
    View function that render users profile
    '''
    profile = Profile.display_member_profile()

    return render(request, 'members/profile.html', {"profiles":profile})
