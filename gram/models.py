from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class NewsLetterRecipients(models.Model):
#     name = models.CharField(max_length = 30)
#     email = models.EmailField()

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=400)
    profile_pic = models.ImageField(upload_to='ProfilePicture/')
￼
￼
￼




class Image(models.Model):  












class Profile(models.Model):  