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

    @classmethod
    def get_project(cls, pk):
        return cls.objects.get(id=pk)

    def __str__(self):
        return self.title


RATES = [
    (1, '1- Poor'),
    (2,'2- Bad'),
    (3,'3- Not Satisfying'),
    (4, '4- Not Good'),
    (5,'5- Average'),
    (6,'6- Fair'),
    (7,'7- Good'),
    (8,'8- Better'),
    (9, '9- Best'),
    (10, '10- Excellent'),
]

class Rating(models.Model):
    '''
    Class that handles project rating
    '''
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='ratings', null=True)
    design = models.PositiveSmallIntegerField(choices = RATES, default=0,blank=True)
    usability = models.PositiveSmallIntegerField(choices = RATES, default=0,blank=True)
    content = models.PositiveSmallIntegerField(choices = RATES, default=0,blank=True)
    score = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='authorrates')

    def __str__(self):
        return f'{self.project} Ratings'
