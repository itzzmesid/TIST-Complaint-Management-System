from django.urls import path
from accounts import views

urlpatterns = [
    path('login', views.loginpage, name ='login'),
    path('signup', views.signup, name = 'signup'),
    path('logout', views.logoutUser, name='logout'),
]
