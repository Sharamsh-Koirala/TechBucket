from re import L
from django.forms import ModelForm
from .models import Service, Support, RegisterEvent

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)

        for key,value in self.fields.items():
            value.widget.attrs.update({'class':'input'})

class SupportForm(ModelForm):
    class Meta:
        model = Support
        fields = '__all__'
        exclude = ['issue']
    
    def __init__(self, *args, **kwargs):
        super(SupportForm, self).__init__(*args, **kwargs)

        for key,value in self.fields.items():
            value.widget.attrs.update({'class':'input'})

class RegisterEventForm(ModelForm):
    class Meta:
        model = RegisterEvent
        fields = '__all__'
        exclude = ['issue']
    
    def __init__(self, *args, **kwargs):
        super(RegisterEventForm, self).__init__(*args, **kwargs)

        for key,value in self.fields.items():
            value.widget.attrs.update({'class':'input'})