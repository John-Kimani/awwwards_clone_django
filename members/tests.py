from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class ProfileTestClass(TestCase):
    '''
    Test class for profile model
    '''
    def setUp(self):
        self.user = User(username='kimperria', email='kimperriatest@gmail.com')
        self.profile = Profile(nickname='grand_muller', member_bio='Greatness requires internal toughness')

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))
        self.assertTrue(isinstance(self.profile, Profile))
