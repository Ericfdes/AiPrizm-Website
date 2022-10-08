from django.shortcuts import render
from .models import *

def blog(request):
    
    context= {
       
    }
    return render(request, "blog/blog-sidebar.html", context)

def blog_detail(request, slug_url):
    blog = Blog.objects.get(slug=slug_url)
    context= {
        'Blog': blog, 
    }
    return render(request, "blog/blog-single.html", context)

def blog_grid(request):
   
    context= {
        
    }
    return render(request, "blog/blog-grid.html", context)

# Create your views here.
