

from django.db import models
from django.template.defaultfilters import slugify

from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
# Create your models here.


STATUS=(
    (0,"Draft"),
    (1,"Publis")
)

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, blank=True, allow_unicode=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True, blank=True, related_name='blog_posts')

    blog_content = RichTextField()
    publish_date = models.DateField(auto_now_add=True, blank=True)
    update_date = models.DateField(auto_now_add=True, blank=True)
    blog_img = models.ImageField(null=True, upload_to="blogpost_imgs/")
    status = models.IntegerField(choices=STATUS, default=0)

    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    tags = TaggableManager()


    class Meta:
        ordering=['-publish_date']

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Blog,self).save(*args,**kwargs)
    
    def __str__(self):
        return f"Blog: {self.title} - {self.author}"
    
    def tags_list(self):
        return self.tags.split(',')

class Author(models.Model):
    author = models.CharField(max_length=100)
    author_desc = models.CharField(max_length=200, null=True)

    twitter = models.CharField(max_length=200, default="#")
    facebook = models.CharField(max_length=200, default="#")
    instagram = models.CharField(max_length=200, default="#")

    def __str__(self):
        return self.author
    
class Category(models.Model):
    category=models.CharField(max_length=50, default="Other")
    
    
    