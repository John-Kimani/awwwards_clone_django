from django.urls import path
from . import views

urlpatterns = [
    path('api/projects/', views.ProjectsData.as_view()),
    path('api/profile/', views.ProfileData.as_view()),

]