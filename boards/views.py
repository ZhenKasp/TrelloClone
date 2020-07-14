from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import List, Card


@login_required
def index(request):
    cards = []
    lists = List.objects.filter(user_id=request.user.id)  #Filter lists by user_id
    for list in lists:
        cards.append(Card.objects.filter(list_id=list.id))
    context = { 'lists': lists, 'cards': cards }
    return render(request, 'boards/index.html', context)

        # "lists" : { list1 : [card1, card2, car3] }
