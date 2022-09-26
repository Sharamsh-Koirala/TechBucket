from re import L
from django.forms import ModelForm
from .models import Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)

        for key,value in self.fields.items():
            value.widget.attrs.update({'class':'input'})
        #self.fields['title'].widget.attrs.update({'class':'input'})