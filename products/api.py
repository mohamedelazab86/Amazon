from rest_framework import generics
from .models import Product,Brand
from .serializers import ProductDetailSerializer,ProductListSerializer
from .serializers import BrandDetailSerializer,BrandListSerializer
from .pagination import MyPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters





class ProductlistApi(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductListSerializer
    pagination_class=MyPagination
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['brand', 'flag']
    
    search_fields = ['name']
    
    ordering_fields = ['price']
    

class ProductdetailApi(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductDetailSerializer

class BrandListApi(generics.ListAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandListSerializer
    pagination_class=MyPagination

class BrandDetailApi(generics.RetrieveAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandDetailSerializer