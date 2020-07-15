from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import List, Card
from django.http import HttpResponse

from boards.models import List
from boards.forms import ListForm


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

@login_required
def post(self, request):

    for key, value in request.POST.items():
        print('Key: %s' % (key))
        # print(f'Key: {key}') in Python >= 3.7
        print('Value %s' % (value))
        # print(f'Value: {value}') in Python >= 3.7

    if request.method == 'POST':
        form = ListForm(request.POST)
        print(HttpResponse(request.POST.items()))
        if form.is_valid():
            a = form.cleaned_data['post']
            a = form.save(commit=False)
            a.name = request.name
            print('ok1')
            a.save()
    return render(request, 'boards/index.html', {'form': form})