

from django.db import models






class Info_counter(models.Model):

    counter=models.CharField(max_length=50,default="counter")
    workers=models.IntegerField(null=True)
    support=models.IntegerField(null=True)
    clients=models.IntegerField(null=True)
    project=models.IntegerField(null=True)


    def __str__(self):
        return self.counter





class ServiceDescription(models.Model):
    headDiscription=models.TextField( max_length=500)
    webdev=models.TextField( max_length=500)
    Mlearning=models.TextField( max_length=500)
    dataA=models.TextField( max_length=500)
    appdev=models.TextField(max_length=500, default="none")
    automation=models.TextField(max_length=500, default="none")
    DigitalMarketing=models.TextField(max_length=500, default="none")


    def __str__(self):
        return self.headDiscription 
 
class Services(models.Model):
    service=models.CharField(max_length=50, default="services")
    heading=models.CharField(max_length=50)
    Description=models.TextField(max_length=500)
    
class Contact(models.Model):
    email=models.EmailField(max_length=254)
    subject=models.CharField(max_length=100)
    name=models.CharField(max_length=500)
    message=models.TextField(max_length=5000,default="")



    def __str__(self) :
        return self.email

class Team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    short_desc = models.TextField(max_length=500)
    photo = models.ImageField(upload_to="website/team_pictures/", null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)

    # social media
    twitter = models.CharField(max_length=200, default="#")
    facebook = models.CharField(max_length=200, default="#")
    instagram = models.CharField(max_length=200, default="#")
    linkedin = models.CharField(max_length=200, default="#")

    def __str__(self):
        return self.name


    
# Create your models here.
