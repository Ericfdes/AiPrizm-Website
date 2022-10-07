from email.policy import default
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import ImageField
from django.template.defaultfilters import slugify
# Create your models here.


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE, default='')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey('Author', on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    blog_desc = models.CharField(max_length=200, default = '')
    created_on = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(upload_to="blog/blog_banners/", null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + "-" + str(self.created_on))
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title + " by " +str(self.author)

class Author(models.Model):
    author_name= models.CharField(max_length=100)
    author_desc= models.CharField(max_length=200, null=True)
    author_pic= models.ImageField(upload_to="blog/author_pic/", null=True, blank=True)
    #Socials
    twitter = models.CharField(max_length=200, default="#")
    facebook = models.CharField(max_length=200, default="#")
    instagram = models.CharField(max_length=200, default="#")

    def __str__(self):
        return self.author_name

class Category(models.Model):
    category = models.CharField(max_length=50, default="Other")

    def __str__(self):
        return self.category

class Comment(models.Model):
    user_name= models.CharField(max_length=100)
    user_pic= models.ImageField(upload_to="blog/user_pic/", null=True, blank=True)
    user_address=models.CharField(max_length=50)
    comment= models.CharField(max_length=2000)
    commented_on=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.user_name