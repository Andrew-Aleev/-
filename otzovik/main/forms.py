from .models import *
from django import forms
from django.forms import ModelForm
from django.forms import TextInput, DateInput, EmailInput

import requests

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['name', 'last_name', 'job', 'date_of_dirth', 'phone', 'email']


class TransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ['model', 'number']


class AnketaForm(forms.ModelForm):
    class Meta:
        model = Anketa
        fields = ['number1', 'number2', 'number3', 'number4', 'number5']

class OprosForm(forms.ModelForm):

    class Meta:
        otvet = [
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
        ]
        model = Opros
        fields = [ 'number1', 'number2', 'number3', 'number4', 'number5','text']
        widgets = {
            'number1': forms.RadioSelect(choices=otvet),
            'number2': forms.RadioSelect(choices=otvet),
            'number3': forms.RadioSelect(choices=otvet),
            'number4': forms.RadioSelect(choices=otvet),
            'number5': forms.RadioSelect(choices=otvet),

        }
