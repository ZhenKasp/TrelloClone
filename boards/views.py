from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import List, Card


@login_required
def index(request):
    lists = List.objects.all()
    cards = Card.objects.all()
    context = {'cards': cards, 'lists': lists}
    return render(request, 'boards/index.html', context)
