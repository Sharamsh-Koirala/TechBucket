from django.db import models
from email.policy import default
import uuid

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    feature_image = models.ImageField(null=True, blank=True, default='default.jpg')
    created_by = models.CharField(max_length=200,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    # creating the many to many relationship with the "tag" table
 
    # the relation ship field "Tag" is set as string because
    # the class is defined below, before the "Tag" class was defined
    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        img = ''
        try:
            if self.feature_image.url:
                img = self.feature_image.url
        except:
            img = ''
        return img 
