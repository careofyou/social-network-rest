from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    # extra fields for the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    info = models.TextField(blank=True)
    
    def __str__(self):
        return f'User profile {self.user.username}'

class Category(models.Model):
    # posts category model
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    # post model
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    class Meta:
        ordering = ['-published']
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    # comments model
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
    
    def __str__(self):
        return f'Comment by {self.author.username} for {self.post.title}'