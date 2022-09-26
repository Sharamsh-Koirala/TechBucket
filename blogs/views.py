# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from .forms import BlogForm


def blogs(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request,pk):
    blogObj = Blog.objects.get(id=pk)
    context = {'blog':blogObj}
    return render(request, 'blogs/single-blogs.html',context)

def createBlog(request):
    form = BlogForm()

    if request.method == 'POST':
        #print('FORM DATA:', request.POST)
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogs')

    context = {'form':form}
    return render(request, 'blogs/blog-form.html', context)


def updateBlog(request, pk):
    blog = Blog.objects.get(id=pk)

    form = BlogForm(instance=blog)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blogs')

    context = {'form': form}

    return render(request, 'blogs/blog-form.html', context)


def deleteBlog(request, pk):
    blog = Blog.objects.get(id=pk)

    if request.method == 'POST':
        blog.delete()
        return redirect('blogs')
    return render(request, 'blogs/delete.html',{'object':blog})