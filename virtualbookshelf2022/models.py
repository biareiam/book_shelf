from django.db import models
from django.contrib.auth.models import User


class Post (models.Model):
    title = models.CharField(max_length=255)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)
    #featured_image = models.ImageField(null=True, blank=True, upload_to="images/")
    #featured_image = CloudinaryField('image', default='placeholder')
    #body = RichTextField()
    body = models.TextField()
    category = models.CharField(max_length=255, default="Romance")
    likes = models.ManyToManyField(User, related_name="blog_posts")
    
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title + ' | ' + str(self.username)

    def get_absolute_url(self):
        return reverse('home')

    def total_likes(self):
        return self.likes.count()


