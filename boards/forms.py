from django import forms
from django.forms import ModelForm
from boards.models import List, Card


class ListForm(ModelForm):
    class Meta:
        model = List
        fields = ['name'] #'__all__'


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['name', 'list'] #'__all__'


class ChangeListName(ModelForm):
    class Meta:
        model = List
        fields = ['name']
