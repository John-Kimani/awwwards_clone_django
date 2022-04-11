from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MemberRegisterForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User

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
    current_user = request.user
    print(current_user)
    user = User.objects.get(username=current_user)
    print(user)
    profile = Profile.objects.filter(member=request.user).first()
    form = ProfileUpdateForm
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            update = Profile()
            update.profile_picture = form.cleaned_data['profile_picture']
            update.member_bio = form.cleaned_data['member_bio']
            update.nickname = form.cleaned_data['nickname']
            update.contact = form.cleaned_data['contact']
            update.website = form.cleaned_data['website']
            update.user = current_user
            update.save()
            return redirect('profile')
        
    return render(request, 'members/profile.html', {"profile":profile, "form":form})
