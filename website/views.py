
from django.shortcuts import render
from .models import Infocounter, ServiceDescription



def index(request):
    count=Infocounter.objects.all()
    service=ServiceDescription.objects.all()
    context={
        "count":count,
        "service": service
    }
    return render(request,'website/index.html', context)

def contact(request):
    return render (request,'website/contact.html')

def pricing(request):
    return render (request,'website/pricing.html')

def service(request):

    service=ServiceDescription.objects.all()
    context={
       
        "service": service
    }
    return render (request,'website/service.html',context)
    

def about(request):
    return render (request,'website/about.html')


def project(request):
    return render (request,'website/project.html')


# Create your views here.
