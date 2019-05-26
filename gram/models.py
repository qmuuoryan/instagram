from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from friendship.models import Friend,Follow,Block
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=400)
    profile_pic = models.ImageField(upload_to='ProfilePicture/')
    # profile_avatar = models.ImageField(upload_to='AvatorPicture/')

    def post_save_user_model(sender, instance, created, *args, **kwargs):
        if created:
            try:
                Profile.objects.create(user=instance)
            except:
                pass
    post_save.connect(post_save_user_model, sender=settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()
        
    def update_profile(self):
        self.update()

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains=name)
        return profile

    @classmethod
    def get_profile_by_id(cls, user):
        user_profile = Profile.objects.get(user=id)
        return user_profile

    @classmethod
    def get_profile_by_username(cls,user):
        profile_info = cls.objects.filter(user__contains=user)
        return profile_info


class Image(models.Model):
    image = models.ImageField(upload_to='instagram/')
    image_caption = models.CharField(max_length=600)
    tag_someone = models.CharField(max_length=40,blank=True)
    imageuploader_profile = models.ForeignKey(User, on_delete=models.CASCADE,null='True', blank=True)
    image_likes = models.ManyToManyField('Profile', default=False, blank=True,related_name='likes')

    def __str__(self):
        return self.image_caption


class Comments(models.Model):
    comment = models.CharField(max_length =80,null=True)
    user = models.ForeignKey(User,null=True)
    post = models.ForeignKey(Image,related_name='comments',null=True)
    
    
    def __str__(self):
        return self.author