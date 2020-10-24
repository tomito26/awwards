from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from cloudinary.models import CloudinaryField


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description=models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    project_image = CloudinaryField('project')
    link = models.URLField(max_length=200)
    
    def __str__(self):
        return self.title