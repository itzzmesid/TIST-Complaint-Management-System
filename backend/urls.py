from django import urls
from django.conf.urls import url
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index,name ='index'),
    path('menu', views.menu, name = 'menu'),
    path('dashboard', views.dashboard, name = 'dashboard'),
]
