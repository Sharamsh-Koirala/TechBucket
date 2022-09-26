from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from gallery.models import CustomerTestimonial, Partner
from blogs.models import Blog
from services.forms import RegisterEventForm

def homepage(request):
    customerTestimonials = CustomerTestimonial.objects.all()
    partners = Partner.objects.all()
    blogs = Blog.objects.all()[:5]


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


    context = {'customerTestimonials' : customerTestimonials, 'partners':partners, 'blogs':blogs, 'eventForm':form}
    return render(request, 'index.html', context)


def about_us(request):
    return render(request, 'about-us.html')