from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("home", views.home),
    ppath("signup", views.Signup.as_view())
    
]