from django import forms
from .models import Projects


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