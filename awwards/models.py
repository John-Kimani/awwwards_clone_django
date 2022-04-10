from django.db import models
from members.models import Profile
from cloudinary.models import CloudinaryField

class Projects(models.Model):
    '''
    Class that handles project instances
    '''
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=50)
    article = models.CharField(max_length=500)
    link = models.URLField(max_length=200)
    image = CloudinaryField('images/')
    pub_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title


class Rating(models.Model):
    '''
    Class that handles project rating
    '''
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='ratings', null=True)
    design = models.IntegerField(blank=True)
    usability = models.IntegerField(blank=True)
    content = models.IntegerField(blank=True)
    score = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='authorrates')

    def __str__(self):
        return f'{self.project} Ratings'
