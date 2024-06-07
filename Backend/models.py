from django.db import models

# Create your models here.

class CategoriesDB(models.Model):
    title_category = models.CharField(max_length=100,null=True,blank=True)
    Des_category = models.CharField(max_length=200,null=True,blank=True)
    Img_category = models.ImageField(upload_to="CategoryImages",null=True,blank=True)

class ProductDB(models.Model):
    category_p = models.CharField(max_length=100,null=True,blank=True)
    product = models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    Des_product = models.CharField(max_length=200,null=True,blank=True)
    Img_product = models.ImageField(upload_to="ProductImages",null=True,blank=True)


