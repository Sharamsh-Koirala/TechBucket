from django.contrib import admin
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('service/<str:pk>/', views.service, name="service"),
    path('create-service/', views.createService, name="create-service"),
    path('update-service/<str:pk>/', views.updateService, name="update-service"),
    path('delete-service/<str:pk>/', views.deleteService, name="delete-service"),
    path('support/', views.support, name='support'),
]