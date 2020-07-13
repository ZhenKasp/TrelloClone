from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.shortcuts import render
from django.http import HttpResponse

from users.forms import SignUpForm # not TrelloClone.users.forms

def index(request):
    return render(request, 'boards/index.html')
