
from unicodedata import name
from django.db import models




class Infocounter(models.Model):
    projects=models.CharField(max_length=50,default="21")
    workers=models.IntegerField(null=True)
    support=models.IntegerField(null=True)
    clients=models.IntegerField(null=True)


    def __str__(self):
        return self.projects


class ServiceDescription(models.Model):


    headDiscription=models.CharField( max_length=100)
    webdev=models.CharField( max_length=100)
    Mlearning=models.CharField( max_length=100)
    dataA=models.CharField( max_length=100)
    appdev=models.CharField(max_length=100, default="none")
    automation=models.CharField(max_length=100, default="none")
    DigitalMarketing=models.CharField(max_length=100, default="none")


    def __str__(self):
        return self.headDiscription 
    
class Contact(models.Model):
    email=models.EmailField(max_length=254)
    Phone=models.CharField(max_length=100)
    name=models.CharField(max_length=500)
    message=models.CharField(max_length=5000,default="none")



    def __str__(self) :
        return self.email

    
# Create your models here.
