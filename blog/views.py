from django.shortcuts import redirect, render
from django.contrib import messages
from blog.forms import CommentForm
from .models import *
from django.core.mail import BadHeaderError
from django.http import HttpResponse, JsonResponse

def blog(request):
    
    context= {
       
    }
    return render(request, "blog/blog-sidebar.html", context)

def blog_detail(request, slug_url):
    blog = Blog.objects.get(slug=slug_url)
    

    if request.method == 'POST':
        comment_form= CommentForm(request.POST)
        if comment_form.is_valid():
            
            obj = comment_form.save(commit=False)
            obj.blog= blog
            obj.save()
            # return JsonResponse({'user_name':obj.user_name, 'commented_on':obj.commented_on, 'user_address':obj.user_address, 'body':obj.body})
        

    comment_form= CommentForm()

    context= {
        'Blog': blog, 
        'comment_form': comment_form,
    }

    return render(request, "blog/blog-single.html", context)

def blog_grid(request):
   
    context= {
        
    }
    return render(request, "blog/blog-grid.html", context)

# Create your views here.
