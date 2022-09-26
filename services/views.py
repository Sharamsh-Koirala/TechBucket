from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Service, Support
from .forms import ServiceForm, SupportForm, RegisterEventForm
from .utils import searchServices, paginateServices

def services(request):
    services, search_query = searchServices(request)
    custom_range, services = paginateServices(request, services, 9)
    #services = Service.objects.all()
    context = {'services':services, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'services/services.html', context)

def service(request,pk):
    serviceObj = Service.objects.get(id=pk)
    context = {'service':serviceObj}
    return render(request, 'services/single-service.html',context)

def createService(request):
    form = ServiceForm()

    if request.method == 'POST':
        #print('FORM DATA:', request.POST)
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('services')

    context = {'form':form}
    return render(request, 'services/service-form.html', context)


def updateService(request, pk):
    service = Service.objects.get(id=pk)

    form = ServiceForm(instance=service)

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('services')

    context = {'form': form}

    return render(request, 'services/service-form.html', context)


def deleteService(request, pk):
    service = Service.objects.get(id=pk)

    if request.method == 'POST':
        service.delete()
        return redirect('services')
    return render(request, 'services/delete.html',{'object':service})

def support(request):
    form = SupportForm()

    if request.method == 'POST':
        #print('FORM DATA:', request.POST)
        form = SupportForm(request.POST)
        issue = request.POST.get('issue').strip("['']")

        if form.is_valid():
            support = form.save(commit=False)
            support.issue = issue
            form.save()
            return redirect('support')

    context = {'form':form}
    return render(request, 'services/support.html', context)


def registerEvent(request):
    form = RegisterEventForm()

    if request.method == 'POST':
        #print('FORM DATA:', request.POST)
        form = RegisterEventForm(request.POST)
        issue = request.POST.get('issue').strip("['']")

        if form.is_valid():
            RegisterEvent = form.save(commit=False)
            RegisterEvent.issue = issue
            form.save()
            return redirect('index')

    context = {'eventForm':form}
    return render(request, 'main.html', context)