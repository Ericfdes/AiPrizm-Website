
from django.shortcuts import render
from .models import Infocounter, ServiceDescription, Contact
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, Http404
from .forms import ContactForm



def index(request):
    count=Infocounter.objects.all()
    service=ServiceDescription.objects.all()
    contact=Contact.objects.all()
    context={
        "count":count,
        "service": service,
        "contact": contact
    }
    return render(request,'website/index.html', context)



def contact(request):
   
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            print(form.cleaned_data)
            body = {
                'name': form.cleaned_data['name'],
                'subject': form.cleaned_data['subject'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # return HttpResponse("Your query has been sent.", status=200)
            return HttpResponse("Message sent successfully", status=200)
    
    
    form = ContactForm()
    return render (request,'website/contact.html',{"form":form})



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
