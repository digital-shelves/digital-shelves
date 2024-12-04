from django.contrib import admin
from django.urls import path, include
from rest_framework.urls import urlpatterns
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('api/items/search/', views.getData),
    path('api/auth/login/', views.login_view, name='login'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/check/', views.check_auth, name='check_auth'),
    path('api/items/add/', views.addItem, name='add-item'),
]