from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('submit/project/', views.publish_project, name='submitproject'),
    path('update/project/', views.update_project, name='updateproject'),
]