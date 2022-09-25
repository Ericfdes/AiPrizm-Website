
from django.shortcuts import render
from .models import Infocounter, ServiceDescription, ContactInfo



def index(request):
    count=Infocounter.objects.all()
    service=ServiceDescription.objects.all()
    contact=ContactInfo.objects.all()
    context={
        "count":count,
        "service": service,
        "contact": contact
    }
    return render(request,'website/index.html', context)

def contact(request):
   
    contact=ContactInfo.objects.all()
    context={ 
        "contact": contact
    }
    return render (request,'website/contact.html',context)

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
