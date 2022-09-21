from multiprocessing import context
from django.shortcuts import render
from .models import Infocounter


def index(request):
    count=Infocounter.objects.all()
    context={
        "count":count
    }
    return render(request,'website/index.html', context)

def contact(request):
    return render (request,'website/contact.html')

def pricing(request):
    return render (request,'website/pricing.html')

def service(request):
    return render (request,'website/service.html')

def about(request):
    return render (request,'website/about.html')


def project(request):
    return render (request,'website/project.html')




# Create your views here.
