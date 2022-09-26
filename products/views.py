
from http.client import HTTPResponse
from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Review, Brand, Category
from .forms import ProductForm, ReviewForm
from .utils import searchProducts, paginateProducts


def products(request):
    products, search_query = searchProducts(request)
    custom_range, products = paginateProducts(request, products, 6)

    context = {'products': products,
               'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'products/products.html', context)


def product(request, pk):
    productObj = Product.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.product = productObj
        review.owner = request.user.profile
        review.save()

        productObj.getVoteCount

        messages.success(request, 'Your review was successfully submitted!')
        return redirect('product', pk=productObj.id)

    return render(request, 'products/product-details.html', {'product': productObj, 'form': form})


@login_required(login_url="login")
def createProduct(request):
    profile = request.user.profile
    form = ProductForm()

    if request.method == 'POST':
        newbrands = request.POST.get('newbrands').replace(',',  " ").split()
        newcategories = request.POST.get('newcategories').replace(',',  " ").split()
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = profile
            product.save()

            for brand in newbrands:
                brand, created = Brand.objects.get_or_create(name=brand)
                product.brand.add(brand)

            for category in newcategories:
                category, created = Category.objects.get_or_create(name=category)
                product.category.add(category)

            return redirect('account')

    context = {'form': form}
    return render(request, "products/product_form.html", context)


@login_required(login_url="login")
def updateProduct(request, pk):
    profile = request.user.profile
    product = profile.product_set.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        newbrands = request.POST.get('newbrands').replace(',',  " ").split()
        newcategories = request.POST.get('newcategories').replace(',',  " ").split()

        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            for brand in newbrands:
                brand, created = Brand.objects.get_or_create(name=brand)
                product.brands.add(brand)

            for category in newcategories:
                category, created = Category.objects.get_or_create(name=category)
                product.category.add(category)

            return redirect('account')

    context = {'form': form, 'product': product}
    return render(request, "products/product_form.html", context)


@login_required(login_url="login")
def deleteProduct(request, pk):
    profile = request.user.profile
    product = profile.product_set.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    context = {'object': product}
    return render(request, 'delete_template.html', context)
