from django.contrib import admin
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('hardware_and_appliances', views.hardwareAndAppliances, name="hardware_and_appliances"),
    path('design_and_development', views.designAndDevelopment, name="design_and_development"),
    path('managed_enterprise_solutions', views.managedEnterpriseSolutions, name="managed_enterprise_solutions"),
]