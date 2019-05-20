from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class Profile(models.Model):    