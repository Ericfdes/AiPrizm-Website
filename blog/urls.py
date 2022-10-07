from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
 
from . import views

urlpatterns = [
path('blog/',views.blog_list,name="blog"),
path('blog_view/',views.blog_view,name="blog_view")

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)