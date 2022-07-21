from django.urls import path
from . import views as vw


# routes for api endpoints
urlpatterns = [
    path('', vw.home,name='home'),
    path('api/products/', vw.RetrieveProducts.as_view(),name='allProductDetail'),
    path('api/product/<slug:slug>', vw.GetProductDetails.as_view(),name='productDetail'),
    path('api/add-product', vw.AddProduct.as_view(),name='addProduct'),
    path('api/update-product/<str:product_id>', vw.UpdateProduct.as_view(),name='updateProduct'),
    path('api/delete-product/<str:product_id>', vw.DeleteProduct.as_view(),name='deleteProduct'),
]
