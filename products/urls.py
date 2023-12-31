from django.urls import path
from .views import ProductList,ProductDetail,BrandList,BrandDetail
from .api import ProductdetailApi,ProductlistApi,BrandDetailApi,BrandListApi


urlpatterns = [

    path('brands/', BrandList.as_view()),
    path('brands/<slug:slug>',BrandDetail.as_view()),
    path('', ProductList.as_view()),
    path('<slug:slug>', ProductDetail.as_view()),

    # api
    path('list/api',ProductlistApi.as_view()),
    path('list/api/<int:pk>',ProductdetailApi.as_view()),
    path('brand/list/api',BrandListApi.as_view()),
    path('brand/api/<int:pk>',BrandDetailApi.as_view())
   
]
