from django.urls import path 

from . import views 

urlpatterns = [ 
    path("", views.index, name="index"), 
    path("url/<str:url>", views.make, name="make"), 
    path("info/<str:info>", views.get, name="get")  
] 
