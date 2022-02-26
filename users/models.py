from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ProfileImage = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
# install Pillow
    def save(self):
        super().save()
        
        img = Image.open(self.ProfileImage.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.ProfileImage.path)