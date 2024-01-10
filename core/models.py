""" Module for creating models in Django"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class UserModel(AbstractUser):
    """Class representing a person"""

    email = models.EmailField(max_length=100, unique=True)
    
    def __str__(self):
        return f'{self.username}'
        
class ContactModel(models.Model):
    address = models.CharField(max_length=1000)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return f'{self.email}'
    
class AboutModel(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='about/')
    
    def __str__(self):
        return f'{self.content[:30]}'
    
class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.name}'

class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/')
    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    slug = models.SlugField(blank=True, null=True, max_length=500)
    
    def __str__(self):
        return f'{ self.title }'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogModel, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('blog-detail', kwargs = {'slug': self.slug})
    
class CommentModel(models.Model):
    content = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f'{self.content[:30]}'
