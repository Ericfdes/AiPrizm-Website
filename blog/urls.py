from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
 
from . import views

urlpatterns = [
path('blog/',views.blog,name="blog"),
path('blog_view/',views.blog_view,name="blogview")

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)