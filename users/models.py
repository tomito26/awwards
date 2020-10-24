from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    image = CloudinaryField('profile-photo')
    
    def __str__(self):
        return f'{self.user.username} Profile'