from django.shortcuts import render

def blog(request):
    return render(request,"blog/blog-sidebar.html")

# Create your views here.
