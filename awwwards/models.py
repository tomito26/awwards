from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from cloudinary.models import CloudinaryField
from django.urls import reverse


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description=models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    project_image = CloudinaryField('project')
    link = models.URLField(max_length=200)
    country = models.CharField(max_length=60, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail',kwargs={'pk':self.pk})

    @classmethod
    def search_by_title(cls,search_term):
        post = cls.objects.filter(title__icontains=search_term)
        return post




RATE_CHOICES = [
    (1,'1 - Trash'),
    (2,'2 - Horrible'),
    (3,'3 - Terrible'),
    (4,'4 - Bad'),
    (5,'5 - OK'),
    (6,'6 - nice work'),
    (7,'7 - Good'),
    (8,'8 - Very Good'),
    (9,'9 - Perfect'),
    (10,'10 - Masterpiece')

]

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    text = models.TextField(blank=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
   
    
    def __str__(self):
        
        return self.user.username