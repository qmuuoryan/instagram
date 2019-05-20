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
￼               def post_save_user_model(sender, instance, created, *args, **kwargs):
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
￼




class Image(models.Model):  
    class Image=(models.Model):
    image_name = models.CharField(max_length = 70)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category )
    photo = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls, image_id):
        image = cls.objects.get(pk=id)
        return cls.objects.get(id=image_id)

    @classmethod
    def update_image(cls,id,name,description,location,category):
        image = cls.objects.get(pk=image_id)
        image = cls(name=name,description=description,location=location,category=category)
        image.save()

    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location_name__location__icontains=location)
        return images

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images
    
    
    @classmethod
    def search_by_category(cls,search_term):
        result_search = cls.objects.filter(category__category_name__icontains=search_term)
        return result_search    

    







