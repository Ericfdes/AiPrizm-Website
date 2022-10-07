from django.http import HttpResponse

from .models import *
from django.shortcuts import render
from .models import Blog, Category


def blog_list(request, slug_url):
    blog = Blog.objects.get(slug=slug_url)
    recent_blogs = blog[:3]
    context = {
        'blogs': blog,
        'recent_blogs': recent_blogs
    }
    return render(request,"blog/blog-list.html",context)



def blog_view(request,slug):
    blogs = Blog.objects.filter(status=1).order_by("-publish_date")
    recent_blogs = blogs[:3]
    try:
        data = Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return HttpResponse("<h1> couldn't find the Blog</h1>")

    context = {
        'blogs': data,
        'recent_blogs': recent_blogs
    }
    return render(request,"blog/blog-single.html",context)
# Create your views here.
