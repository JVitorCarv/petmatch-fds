from django import forms
from django.forms import ModelForm

from .models import PetProfile


class PetProfileForm(ModelForm):
     class Meta:
         model = PetProfile
         fields = ['name', 'author', 'age', 'race', 'bio']

         widgets = {
             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your pet name!'}),
             'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'author', 'type':'hidden'}),
             'age': forms.NumberInput(attrs={'class': 'form-control'}),
             'race': forms.TextInput(attrs={'class': 'form-control'}),
             'bio': forms.TextInput(attrs={'class': 'form-text'}),
         }
