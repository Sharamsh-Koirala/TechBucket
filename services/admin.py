from django.contrib import admin

# Register your models here.
from .models import Service
from .models import Support

admin.site.register(Service)
admin.site.register(Support)