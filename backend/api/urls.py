from django.contrib import admin
from django.urls import path, include
from rest_framework.urls import urlpatterns
from . import views

urlpatterns = [
    path('api/', views.getData)
]