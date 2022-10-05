
from http.client import HTTPResponse
from django.shortcuts import render
from .models import *
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from django.contrib import messages



def index(request):
    count=Info_counter.objects.all()
    service=ServiceDescription.objects.all()
    contact=Contact.objects.all()
    testimonial = Testimonial.objects.all()
    context={
        "count":count,
        "service": service,
        "contact": contact,
        "testimonial": testimonial,
        'nbar': 'home' ,
    }
    return render(request,'website/index.html', context)



# def contact(request):
#     form = ContactForm()

# 	if request.method == 'POST':

# 		form = ContactForm(request.POST)
# 		if form.is_valid():
# 			subject = "Website Inquiry" 
# 			body = {
# 			'name': form.cleaned_data['name'], 
# 			'subject': form.cleaned_data['subject'], 
# 			'email': form.cleaned_data['email'], 
# 			'message':form.cleaned_data['message'], 
# 			}
# 			message = "\n".join(body.values())

# 			try:
# 				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
# 			except BadHeaderError:
# 				return HttpResponse('Invalid header found.')
# 			# return render (request,"website/contact.html")
           
#     context={'nbar': 'contact', 'form': form}
# 	return render(request, "website/contact.html", {'form':form})

def contact(request):
    form  = ContactForm()

    if request.method == 'POST':
        
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'name': form.cleaned_data['name'],
                'subject': form.cleaned_data['subject'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            messages.success(request, 'Form submission successful')
            form.save()

            try:
                send_mail(subject, message, 'agnelofernandes@gmail.com',['howis@gmail.com'])
            except BadHeaderError:
                return HTTPResponse('Invalid header found.')
            # return HttpResponse("Your query has been sent.", status=200)

    context={'nbar': 'contact', 'form': form}
    return render(request, 'website/contact.html', context)

def service(request):

    service=ServiceDescription.objects.all()
    team=Team.objects.all().order_by("order")
    context={
       
        "service": service,
		 "team": team, 
         'nbar': 'service'
    }
    return render (request,'website/service.html',context)
    

def about(request):
    
    team=Team.objects.all().order_by("order")
    context={
       
        
		 "team": team,
         'nbar': 'about',
    }
    return render (request,'website/about.html',context)


def project(request):
    context = {
        'nbar' : 'project'
    }
    return render (request,'website/project.html', context)

def blog(request):
    context = {
        'nbar': 'blog',
    }
    return render(request, 'website/blog-grid.html')
