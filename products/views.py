from django.shortcuts import render
from .models import Product,Review,ProdImage,Brand
from django.views.generic import ListView,DetailView


# Create your views here.
# def test(request):
#     data=Product.objects.all()
#     context={'data':data}
#     return render(request,'products/test.html',context)


class ProductList(ListView):
    model=Product
    paginate_by=50

class ProductDetail(DetailView):
    model=Product

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context["images"] = ProdImage.objects.filter(product=self.get_object())
        context["related"] = Product.objects.filter(brand=self.get_object().brand)

        
        return context
class BrandList(ListView):
    model=Brand
    paginate_by=20

class BrandDetail(ListView):
    model=Product
    template_name='products/brand_detail.html'
    paginate_by=2

    def get_queryset(self):
        brand=Brand.objects.get(slug=self.kwargs['slug'])
        queryset=super().get_queryset().filter(brand=brand)

                                
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context
    

        
    

  
    

# class BrandDetail(DetailView):
#     model=Brand

#     def get_context_data(self, **kwargs) :
#         context = super().get_context_data(**kwargs)
#         context["related"] =Product.objects.filter(brand=self.get_object()) 
#         return context
    

    
    
    

