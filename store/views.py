from turtle import color
from unicodedata import name
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from .serializers import ProductSerializer
from .models import Product,Category,Tag,Images
from store import serializers

# Create your views here.

# @api_view(['POST'])
# def addProduct(request):
#     data = request.data
#     img = request.FILES['img']

class AddProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self,request):
        data = request.data

        product = Product(name=data['name'],description=data['description'],actualPrice=data['actualPrice'],discountedPrice=data['discountedPrice'],quantity=data['quantity'],countryOfOrigin=data['countryOfOrigin'],color=data['color'])
        product.save()
        for category in data['categories'].split(','):
            try:
                # catg = Category.objects.get(name=category['name'])
                catg = Category.objects.get(name=category)
            except:
                catg = Category.objects.create(name=category)
                # catg = Category.objects.create(name=category['name'])
            product.categories.add(catg)
        
        for tag in data['tags'].split(','):
            try:
                t = Tag.objects.get(name=tag)
            except:
                t = Tag.objects.create(name=tag)
            product.tags.add(t)
        
        for img in data['prodImages']:
            # try:
            #     i = Images.objects.get(name=img['prodImages'])
            # except:
            i = Images.objects.create(img=img['prodImages'])
            product.prodImages.add(i)
            # print(img)

        # serializer = ProductSerializer(product)
        return Response({'msg':'done'})
        # return Response(serializer.data)

# @api_view(['GET'])
# def getProductDetails(request,product_slug):
#     product = Product.objects.get(slug = product_slug)
#     serializer = ProductSerializer(product)
#     return Response(serializer.data)


class GetProductDetails(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    lookup_field = 'slug'
    serializer_class = ProductSerializer
