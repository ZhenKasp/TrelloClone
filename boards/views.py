from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import List, Card


@login_required
def index(request):
    dictionary = {}
    lists = List.objects.filter(user_id=request.user.id)  #Filter lists by user_id
    for list in lists:
        cards = Card.objects.filter(list_id=list.id)
        dictionary[list.name] = cards
    context = { 'dictionary': dictionary }
    return render(request, 'boards/index.html', context)

        # "lists" : { list1 : [card1, card2, car3] }
