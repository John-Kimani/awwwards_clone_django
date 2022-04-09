from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone


class Profile(models.Model):
    member = models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE)
    profile_picture = CloudinaryField('images/')
    member_bio = models.TextField(max_length=50, blank=True)
    date_joined = models.DateField(default=timezone.now)
    nickname = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.nickname
