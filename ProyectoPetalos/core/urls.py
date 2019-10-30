from django.contrib import admin
from django.urls import path,include #agregar libreria "include"
from .views import index

urlpatterns = [
    path('',index,name='INDEX'), #renderizar pag index
]