from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics

from .serializers import ProductSerializer
from .models import Product
from .serializers import ProductSerializer


def home(request):
    return render(request,'store/index.html')

class AddProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self,request):
        data = request.data
        print(data)
        prodImages = data.pop('prodImages')
        categories = data.pop('categories')
        tags = data.pop('tags')

        serializer = self.serializer_class(data=data, context={"images":prodImages,"categories":categories,"tags":tags})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



class GetProductDetails(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    lookup_field = 'slug'
    serializer_class = ProductSerializer


class UpdateProduct(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = "product_id"

class DeleteProduct(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'


class RetrieveProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer