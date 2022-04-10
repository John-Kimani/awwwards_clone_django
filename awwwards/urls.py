"""awwwards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from members import views as members_views
from api.views import ProjectsData as project_views
from api.views import ProfileData as profile_views
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('awwards.urls')),

    #members app
    path('register/', members_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='members/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='members/logout.html'), name='logout'),
    path('profile/', members_views.member_profile, name='profile'),

    #backend-apis
    path('api/', include('api.urls')),

    path('api/projects/', views.ProjectsData.as_view()),
    path('api/profile/', views.ProfileData.as_view()),

]
