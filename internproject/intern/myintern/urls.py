# from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.homepage, name="homepageName"),
    path('form/', views.formInput, name="formInputName"),
    path('login/', views.user_login, name="loginName"),
    path('register/', views.user_register, name="registerName"),
    path('logout/', views.user_logout, name="logoutName"),
]
