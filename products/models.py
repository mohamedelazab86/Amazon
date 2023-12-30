from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
# create data base here
class Product(models.Model):
    flag_type=[
        ('New','New'),
        ('Sale','Sale'),
        ('Feature','Feature'),
               ]
    name=models.CharField(max_length=120,verbose_name=_('name'))
    flag=models.CharField(max_length=50,choices=flag_type)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    image=models.ImageField(upload_to='product_image')
    sku=models.IntegerField(unique=True)
    subtitle=models.TextField(max_length=4000)
    descriptions=models.TextField(max_length=50000)
    brand=models.ForeignKey('Brand',on_delete=models.SET_NULL,null=True,related_name='product_brand')
    slug=models.SlugField(null=True,blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Product,self).save(*args,**kwargs)
class Brand(models.Model):
    name=models.CharField(max_length=120)
    image=models.ImageField(upload_to='brand_image')

    slug=models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Brand,self).save(*args,**kwargs)
class ProdImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='proimage_product')
    images=models.ImageField(upload_to='images')

    def __str__(self):
        return str(self.product)
    
class Review(models.Model):
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='review_author')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='revgiew_product')
    review=models.TextField(max_length=2000)
    rate=models.IntegerField(choices=[(i,i) for i in range(1,6)])
    publish_date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.author)
    




        
