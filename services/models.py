from django.db import models
from email.policy import default
import uuid

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg")

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url

class Support(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    email = models.EmailField(max_length = 254, null=False, blank=False)
    address = models.CharField(max_length=200)
    issue = models.CharField(max_length=200)
    details = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class RegisterEvent(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    email = models.EmailField(max_length = 254, null=False, blank=False)
    address = models.CharField(max_length=200)
    details = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name