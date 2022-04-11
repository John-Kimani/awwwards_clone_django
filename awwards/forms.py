from django import forms
from .models import Projects,Rating


class ProjectSubmissionForm(forms.ModelForm):
    '''
    Class that handles project submission
    '''
    class Meta:
        model = Projects
        fields = '__all__'

class UpdateProjectForm(forms.ModelForm):
    '''
    Class that handles project update
    '''
    class Meta:
        model = Projects
        fields = '__all__'
        exclude = ['user','pub_date']

class RateProjectForm(forms.ModelForm):
    '''
    Class that handles ratings
    '''
    class Meta:
        model = Rating
        fields = '__all__'