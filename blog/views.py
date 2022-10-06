from django.shortcuts import render

def blog(request):
    return render(request, "blog/blog-sidebar.html")

def blog_detail(request):
    return render(request, "blog/blog-single.html")

# Create your views here.
