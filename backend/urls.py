from django.urls import path

from .views import HelloView, ProductView, StoreView
# import .views

urlpatterns = [
    path('hello/', HelloView.as_view()),
    path('product/', ProductView.as_view()),
    path('product/<str:branch>', ProductView.as_view()),
    path('storeproducts/', StoreView.as_view()),
    path('store/', StoreView.as_view()),
    # path('price/<str:name>', StoreView.as_view()),

]