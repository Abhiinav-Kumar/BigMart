from django.db import models

# Create your models here.

class ContactDB(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    Subject = models.CharField(max_length=100,null=True,blank=True)
    Messages = models.CharField(max_length=200,null=True,blank=True)

class UserDB(models.Model):
    Username = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Pass = models.CharField(max_length=20,null=True,blank=True)

class cartDB(models.Model):
    Username = models.CharField(max_length=100,null=True,blank=True)
    ProductName = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    TotalPrice = models.IntegerField(null=True,blank=True)

