from django.urls import path

from .views import ProductView, StoreView, Product_Store_View
# import .views

urlpatterns = [
    # path('hello/', HelloView.as_view()),
    path('product', ProductView.as_view()),
    path('product/<int:id>', ProductView.as_view()),
    path('store', StoreView.as_view()),
    path('stores/<int:id>/products/', Product_Store_View.as_view()),
    path('price', Product_Store_View.as_view()),

]