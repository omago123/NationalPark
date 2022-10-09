from .models import test,state
from django import forms

class testForm(forms.ModelForm):
    class Meta:
        model = test
        fields = ['park_latitude','park_longitude']

class stateForm(forms.ModelForm):
    class Meta:
        model = state
        fields = ['name','lat','lng']