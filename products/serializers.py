from rest_framework import serializers
from .models import Product,Brand,Review,ProdImage

class ProImageSerailizer(serializers.ModelSerializer):
    class Meta:
        model=ProdImage
        fields=['images']
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['user','rate']

    
class ProductListSerializer(serializers.ModelSerializer):
   

    class Meta:
        model=Product
        fields='__all__'
    
        

class ProductDetailSerializer(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    review_count=serializers.SerializerMethodField()
    avg=serializers.SerializerMethodField()
    images=ProImageSerailizer(source='proimage_product',many=True)
    reviews=ReviewSerializer(source='revgiew_product',many=True)
    class Meta:
        model=Product
        fields='__all__'
        
    def get_review_count(self,object):
        reviews=object.revgiew_product.all().count()
        return reviews
    
    def get_avg(self,object):
        total=0
        reviews=object.revgiew_product.all()
        if len(reviews):
            for item in reviews:
                total +=item.rate
            avg=total/len(reviews)
        else:
            avg=0

        return avg
    




class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'

class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'
