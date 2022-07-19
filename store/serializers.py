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
    # categories = serializers.SerializerMethodField()
    # tags = serializers.SerializerMethodField()
    # prodImages =  serializers.SerializerMethodField()
    categories = CategorySerializer(many=True)
    tags = TagSerializer(many=True)
    prodImages =  ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'

    




