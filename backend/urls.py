from django.urls import path

from .views import HelloView
# import .views

urlpatterns = [
    path('hello/', HelloView.as_view()),

]