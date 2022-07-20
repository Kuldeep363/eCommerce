from django.urls import path
from . import views as vw

urlpatterns = [
    path('products/', vw.RetrieveProducts.as_view(),name='allProductDetail'),
    path('product/<slug:slug>', vw.GetProductDetails.as_view(),name='productDetail'),
    path('add-product', vw.AddProduct.as_view(),name='addProduct'),
    path('update-product/<str:product_id>', vw.UpdateProduct.as_view(),name='updateProduct'),
    path('delete-product/<str:product_id>', vw.DeleteProduct.as_view(),name='deleteProduct'),
]
