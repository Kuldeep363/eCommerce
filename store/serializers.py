from math import prod
from pyexpat import model
from unicodedata import category
from attr import fields
from rest_framework import serializers
from .models import Category,Tag,Images,Product



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        depth = 1

    

    def create(self,validated_data):
        images = self.context['images']
        categories = self.context['categories'][0].split(',')
        tags = self.context['tags'][0].split(',')
        print(f'c:{categories}')
        print(f't:{tags}')
        print(validated_data)
        print(f'i:{images}')

        # return 1
        product = Product(**validated_data)
        product.save()
        for category in categories:
            try:
                catg = Category.objects.get(name=category)
            except:
                catg = Category.objects.create(name=category)
            product.categories.add(catg)
        
        for tag in tags:
            try:
                t = Tag.objects.get(name=tag)
            except:
                t = Tag.objects.create(name=tag)
            product.tags.add(t)

        for img in images:
            imgObject = Images.objects.create(img = img)
            imgObject.slug += str(imgObject.id)
            product.prodImages.add(imgObject)
        
        return product





