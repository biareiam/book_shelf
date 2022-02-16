from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return str(self.user)


class Post (models.Model):
    title = models.CharField(max_length=255)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)
    #featured_image = models.ImageField(null=True, blank=True, upload_to="images/")
    featured_image = CloudinaryField('image', default='placeholder')
    body = RichTextField()
    category = models.CharField(max_length=255, default="Romance")
    likes = models.ManyToManyField(User, related_name="blog_posts")
    #profile_image = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    

    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title + ' | ' + str(self.username)

    def get_absolute_url(self):
        return reverse('home')

    def total_likes(self):
        return self.likes.count()