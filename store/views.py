from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics

from .serializers import ProductSerializer
from .models import Product
from .serializers import ProductSerializer


# index page
def home(request):
    return render(request,'store/index.html')


# add product in DB
class AddProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # overriding create method
    def create(self,request):
        data = request.data                                 #collecting data from api request
        prodImages = data.pop('prodImages')                 #extracting images
        categories = data.pop('categories')                 #extracting categories
        tags = data.pop('tags')                             #extracting tags, so that we can create product object easily and also can add these fields with product later

        serializer = self.serializer_class(data=data, context={"images":prodImages,"categories":categories,"tags":tags})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


# retrieving product using slug
class GetProductDetails(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    lookup_field = 'slug'
    serializer_class = ProductSerializer

# updating product by targeting "id" of the product
class UpdateProduct(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = "product_id"

# deleting product by targeting "id" of the product
class DeleteProduct(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'

# retrieving all the products in the DB
class RetrieveProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer