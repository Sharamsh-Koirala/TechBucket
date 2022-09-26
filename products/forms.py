from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from .models import Product, Review, Brand, Category


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'specification', 'featured_image', 'description',
                  'demo_link','source_link']
        widgets = {
            'category': forms.CheckboxSelectMultiple(),
            'brand': forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update(
        #     {'class': 'input'})

        # self.fields['description'].widget.attrs.update(
        #     {'class': 'input'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['body']

        labels = {
            'body': 'Add a comment with your vote',
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
