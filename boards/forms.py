from django import forms
from django.forms import ModelForm
from boards.models import List

class ListForm(ModelForm):
    class Meta:
        model = List
        fields = '__all__'