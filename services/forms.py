from dataclasses import fields
from django.core import validators
from django import forms
from .models import Driver

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['id', 'name', 'complaint']