'''
Created on 29-Jun-2015

@author: anshul
'''
from django import forms
from chronassist.models import Item

class ItemForm(forms.ModelForm):
    model = Item