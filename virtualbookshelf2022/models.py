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
    first_name = models.CharField(max_length=255, default='Mary')
    last_name = models.CharField(max_length=255, default='Ann')
    email = models.EmailField(default='my@email.com')


    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('home')


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

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_addded = models.DateTimeField(auto_now_add=True)
    #likes = models.ManyToManyField(User, related_name="blog_posts")

    class Meta:
        ordering = ["-date_addded"]
    
    def __str__(self):
        return '%s -%s' % (self.post.title, self.name)

    
