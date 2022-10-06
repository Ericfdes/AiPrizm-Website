from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blog_grid/', views.blog_grid, name='blog_grid'),
    path('blog_detail/<str:slug_url>', views.blog_detail, name='blog_detail'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)