from django.db import models

import uuid

from django.db.models.deletion import CASCADE
# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=200,default="")
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200)
    specification = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    featured_image_2 = models.ImageField(null=True, blank=True, default="default.jpg")
    featured_image_3 = models.ImageField(null=True, blank=True, default="default.jpg")
    featured_image_4 = models.ImageField(null=True, blank=True, default="default.jpg")
    featured_image_5 = models.ImageField(null=True, blank=True, default="default.jpg")

    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    category = models.ManyToManyField('Category', blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)


    def __str__(self):
        return self.title

    #class Meta:
    #   ordering = ['-vote_ratio', '-vote_total', 'title']

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url

    # @property
    # def reviewers(self):
    #     queryset = self.review_set.all().values_list('owner__id', flat=True)
    #     return queryset

   

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.value



class Category(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
