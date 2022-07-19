from django.utils.text import slugify
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False,default='category##',unique=True)
    slug = models.SlugField(unique=True,blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args,**kwargs)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False,default='tag##',unique=True)
    slug = models.SlugField(unique=True,blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Tag,self).save(*args,**kwargs)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Images(models.Model):
    img = models.ImageField(upload_to='uploads/',blank=True,null=True)
    slug = models.SlugField(unique=True,blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.img)
        super(Images,self).save(*args,**kwargs)

    def __str__(self):
        return self.slug


class Product(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False,default='product##')
    description = models.TextField()
    prodImages = models.ManyToManyField(Images,related_name='productImage', blank=True,null=True)
    actualPrice = models.FloatField(null=False,blank=False,default=0)
    discountedPrice = models.FloatField(null=False,blank=False,default=0)
    quantity = models.IntegerField(null=False,blank=False,default=0)
    countryOfOrigin = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    categories = models.ManyToManyField(Category, related_name='productCategories')
    tags = models.ManyToManyField(Tag,related_name='productTags')
    dateAdded = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    slug = models.SlugField(unique=True,blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Product,self).save(*args,**kwargs)


    # def img_url(self):
    #     if self.prodImage:
    #         for img in self.prodImages:
    #         return self.prodImage.url
    #     return ''

    def __str__(self):
        return self.slug
