from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name="home"), 
    path('add/',views.add,name="add"),
    path('delete/',views.delete,name="delete"),
    path('update/',views.update,name="update"), 
    path('read/',views.read,name="read"),

    
]
