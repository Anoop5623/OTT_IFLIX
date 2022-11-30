from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('signup',signup,name="handlesignup"),
    path('login',handlelogin,name="login"),
    path('logout',handlelogout,name="handlelogout"),
    path('',home),
    ]
