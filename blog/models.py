from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey('Author', on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Author(models.Model):
    author_name= models.CharField(max_length=100)
    author_desc= models.CharField(max_length=200, null=True)
    #Socials
    twitter = models.CharField(max_length=200, default="#")
    facebook = models.CharField(max_length=200, default="#")
    instagram = models.CharField(max_length=200, default="#")

    def __str__(self):
        return self.author

class Category(models.Model):
    category = models.CharField(max_length=50, default="Other")

    def __str__(self):
        return self.category