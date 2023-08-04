from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("home", views.home),
    path("signup", views.Signup.as_view()),
    path("login", views.Login.as_view())

]
