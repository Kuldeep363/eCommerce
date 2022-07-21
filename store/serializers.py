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
        images = self.context['images']                                 # getting images from context passed in AddProduct class of views.py file
        
        product = Product(**validated_data)                             # creating product object
        product.save()

        # adding categories with product
        # if category is not in DB alrady, creating it and then adding with product
        try:
            categories = self.context['categories'][0].split(',')           # converting comma separated categories string into list of categories
            for category in categories:
                try:
                    catg = Category.objects.get(name=category)
                except:
                    catg = Category.objects.create(name=category)
                product.categories.add(catg)
        except:
            pass

        
        # adding tags with product
        # if tag is not in DB alrady, creating it and then adding with product
        try:
            tags = self.context['tags'][0].split(',')  
            for tag in tags:
                try:
                    t = Tag.objects.get(name=tag)
                except:
                    t = Tag.objects.create(name=tag)
                product.tags.add(t)
        except:
            pass

        # adding image with the product
        for img in images:
            imgObject = Images.objects.create(img = img)
            imgObject.slug += str(imgObject.id)
            product.prodImages.add(imgObject)
        
        return product





