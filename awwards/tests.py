from django.test import TestCase
from .models import Projects,Rating


class ProjectTestClass(TestCase):
    '''
    Class that tests Project model
    '''
    def setUp(self):
        self.project = Projects(title='Showman', article='This is the greatest show')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.project, Projects))



class RatingTestClass(TestCase):
    '''
    Class that test rating model
    '''
    def setup(self):
        self.rates = Rating(design=10,usability=10, content=10, score=10)

    def test_instance(self):
        self.assertTrue(isinstance(self.rates, Rating))
