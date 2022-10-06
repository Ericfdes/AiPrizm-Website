from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from website import views

urlpatterns = [
    path('',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
 
    path('project/',views.project,name="project"),
    path('service/',views.service,name="service"),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)