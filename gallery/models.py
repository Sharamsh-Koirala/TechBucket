from email.policy import default
from django.db import models
import uuid
# Create your models here.

class CompanyEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #feature_image = models.ImageField(null=True, blank=True, default='default.jpg')
    #feature_images = models.FileField(upload_to='images/%Y/%m/%d')
    video_link = models.CharField(max_length=1000,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.title

class CompanyEventPhoto(models.Model):
    companyEvent = models.ForeignKey(
        CompanyEvent, on_delete=models.CASCADE, related_name="feature_images"
    )
    feature_images = models.ImageField()

class CustomerTestimonial(models.Model):
    name = models.CharField(max_length=200,null=False, blank=False)
    title = models.CharField(max_length=200,null=False, blank=False)
    description = models.TextField()
    ct_image = models.ImageField(null=False, blank=False)
    video_link = models.CharField(max_length=1000,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        img = ''
        try:
            if self.ct_image.url:
                img = self.ct_image.url
        except:
            img = ''
        return img     

class PromotionalVideo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_link = models.CharField(max_length=1000,null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Partner(models.Model):
    title = models.CharField(max_length=200)
    partner_logo = models.ImageField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        img = ''
        try:
            if self.partner_logo.url:
                img = self.partner_logo.url
        except:
            img = ''
        return img     