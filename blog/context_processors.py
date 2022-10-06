from blog.models import *

def context_base(request):
    blog = Blog.objects.all()
    return { 'Blog': blog}