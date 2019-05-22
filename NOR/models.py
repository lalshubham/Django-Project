from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
    body = models.CharField(max_length=250)
    thumb = models.ImageField(default='default.png',blank=True)
    author_name = models.CharField(max_length=30, blank=True)
    AuthorsName = models.ForeignKey(User,default=None)
    date = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return self.slug, self.title

    def snippet(self):
        return self.body[0:150] +'   '


class Roles(models.Model):
    name = models.CharField(max_length=30)
    display_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Coupons(models.Model):
    Code = models.CharField(max_length=30)
    Code_Type = models.CharField(max_length=30)
    value = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Code

class Addresses(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name