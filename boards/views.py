from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from boards.models import List, Card
from boards.forms import ListForm, CardForm


@login_required
def index(request):

    dictionary = {}
    lists = List.objects.filter(user_id=request.user.id)  #Filter lists by user_id
    for list in lists:
        cards = Card.objects.filter(list_id=list.id)
        dictionary[list] = cards

    if request.method == 'POST':

        form_card = CardForm(request.POST)
        if form_card.is_valid():
            a = form_card.save(commit=False)
            a.user = request.user
            a.save()
            return redirect('index')  # using GET request, for reloading the page without submitting form again

        form_list = ListForm(request.POST)
        if form_list.is_valid():
            a = form_list.save(commit=False)
            a.user = request.user
            a.save()
            return redirect('index')

    else:
        form_list = ListForm()
        form_card = CardForm()

    forms_dict = {'form_list': form_list, 'form_card': form_card}
    context = {'dictionary': dictionary, 'form': forms_dict} # dictionary == "lists" : { list1 : [card1, card2, car3] }
    return render(request, 'boards/index.html', context)