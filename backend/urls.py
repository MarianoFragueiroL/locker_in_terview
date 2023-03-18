from django.urls import path

from .views import HelloView, ProductView, StoreView, Product_Store_View
# import .views

urlpatterns = [
    path('hello/', HelloView.as_view()),
    path('product/', ProductView.as_view()),
    path('product/<str:branch>', ProductView.as_view()),
    path('store/', StoreView.as_view()),
    path('storeproducts/<str:name>', Product_Store_View.as_view()),
    path('price/', Product_Store_View.as_view()),

]