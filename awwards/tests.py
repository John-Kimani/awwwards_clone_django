from django.test import TestCase
from .models import Projects


class ProjectTestClass(TestCase):
    '''
    Class that tests Project model
    '''
    def setUp(self):
        self.project = Projects(title='Showman', article='This is the greatest show')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.project, Projects))
