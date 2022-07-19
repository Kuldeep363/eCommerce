from django.contrib import admin

from .models import Category,Images,Tag,Product

# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Images)
admin.site.register(Product)
