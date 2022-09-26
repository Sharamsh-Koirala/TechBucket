from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from .models import CompanyEvent, CustomerTestimonial, PromotionalVideo, CompanyEventPhoto, Partner
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext as _

class CompanyEventForm(forms.ModelForm):
    class Meta:
        model = CompanyEvent
        fields = ("title", "description", "video_link")
        #feature_images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        # widgets = {
        #     'feature_images': forms.ClearableFileInput(attrs={'multiple': True}),
        # }
        feature_images = forms.FileField(
            widget=forms.ClearableFileInput(attrs={"multiple": True}),
            label=_("Add photos"),
            required=False,
        )
        
    # def __init__(self, *args, **kwargs):
    #     super(CompanyEventForm, self).__init__(*args, **kwargs)

    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'input'})
        
        #self.fields['feature_images'].widget.attrs.update({'class': 'input','multiple': True})
        #file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))    
    
    def clean_photos(self):
        """Make sure only images can be uploaded."""
        for upload in self.files.getlist("feature_images"):
            validate_image_file_extension(upload)

    def save_photos(self, companyEvent):
        """Process each uploaded image."""
        for upload in self.files.getlist("feature_images"):
            photo = CompanyEventPhoto(companyEvent=companyEvent, photo=upload)
            photo.save()

class CustomerTestimonialForm(ModelForm):
    class Meta:
        model = CustomerTestimonial
        fields = ['title', 'ct_image', 'description', 'video_link']

    def __init__(self, *args, **kwargs):
        super(CustomerTestimonial, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class PromotionalVideoForm(ModelForm):
    class Meta:
        model = PromotionalVideo
        fields = ['title', 'description', 'video_link']

    def __init__(self, *args, **kwargs):
        super(PromotionalVideo, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields = ['title', 'partner_logo']

    def __init__(self, *args, **kwargs):
        super(Partner, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})