from django.contrib import admin
from .forms import CompanyEventForm

# Register your models here.

from .models import CompanyEvent, CustomerTestimonial, PromotionalVideo, CompanyEventPhoto, Partner

admin.site.register(CompanyEvent)
admin.site.register(CustomerTestimonial)
admin.site.register(PromotionalVideo)
admin.site.register(CompanyEventPhoto)
admin.site.register(Partner)
#@admin.register(CompanyEventPhoto)



class ShowPhotoInline(admin.TabularInline):
    model = CompanyEventPhoto

class ShowCompanyEvent(admin.ModelAdmin):
    form = CompanyEventForm
    inlines = [ShowPhotoInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)