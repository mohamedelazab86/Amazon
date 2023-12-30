from django.contrib import admin
from .models import ProdImage,Product,Review,Brand
from django_summernote.admin import SummernoteModelAdmin



class Imageadmin(admin.TabularInline):
    model=ProdImage


class productadmin(SummernoteModelAdmin):

    list_display=['name','flag','sku']
    list_filter=['flag','brand']
    search_fields=['name']
    summernote_fields = ('subtitle','descriptions')
    inlines=[Imageadmin]

# Register your models here.

admin .site.register(Product,productadmin)
admin .site.register(Review)
admin .site.register(Brand)
#admin .site.register(ProdImage)

