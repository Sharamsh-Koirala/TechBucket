from django.shortcuts import render, redirect
from django.http import HttpResponse
from gallery.models import CustomerTestimonial

def hardwareAndAppliances(request):
    customerTestimonials = CustomerTestimonial.objects.all()
    context = {'customerTestimonials' : customerTestimonials}
    return render(request, 'pages/hardware_and_appliances.html', context)

def designAndDevelopment(request):
    customerTestimonials = CustomerTestimonial.objects.all()
    context = {'customerTestimonials' : customerTestimonials}
    return render(request, 'pages/design_and_development.html', context)

def managedEnterpriseSolutions(request):
    customerTestimonials = CustomerTestimonial.objects.all()
    context = {'customerTestimonials' : customerTestimonials}
    return render(request, 'pages/managed_enterprise_solutions.html', context)