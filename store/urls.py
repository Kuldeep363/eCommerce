from django.urls import path
from . import views as vw

urlpatterns = [
    path('product/<slug:slug>', vw.GetProductDetails.as_view(),name='productDetail'),
    path('add-product', vw.AddProduct.as_view(),name='addProduct'),
]
