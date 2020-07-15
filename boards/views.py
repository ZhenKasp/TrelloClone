from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import List, Card
from django.http import HttpResponse

from boards.models import List
from boards.forms import ListForm


@login_required
def index(request):
    dictionary = {}
    list1 = []
    lists = List.objects.filter(user_id=request.user.id)  #Filter lists by user_id
    for list in lists:
        cards = Card.objects.filter(list_id=list.id)
        dictionary[list.name] = cards

    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid(): # <-- doesn't go past here!
            a = form.save(commit=False)
            a.name = request.name
            a.save()
        list1 = List.objects.all()

    context = {'dictionary': dictionary, 'list': list1}
    print(request.POST, context)
    return render(request, 'boards/index.html', context)
# "lists" : { list1 : [card1, card2, car3] }