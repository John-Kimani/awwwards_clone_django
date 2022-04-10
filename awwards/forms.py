from django import forms
from .models import Projects


class ProjectSubmissionForm(forms.ModelForm):
    '''
    Class that handles porject submission
    '''
    class Meta:
        model = Projects
        fields = '__all__'