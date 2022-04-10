from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone


class Profile(models.Model):
    member = models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE, blank=True, null=True)
    profile_picture = CloudinaryField('images/', default='https://res.cloudinary.com/dbgbail9r/image/upload/v1649544556/profile_image_kfrlhw.png')
    member_bio = models.TextField(max_length=50, blank=True)
    date_joined = models.DateField(default=timezone.now)
    nickname = models.CharField(max_length=10, null=True, blank=True)
    contact = models.CharField(max_length=15, blank=True, null=False)
    website = models.URLField(max_length=200, blank=True, null=False)


    # @classmethod
    # def display_member_profile(cls):
    #     '''
    #     Function that displays members information
    #     '''
    #     profile = cls.objects.all()
    #     return profile

    def __str__(self):
        return self.nickname
