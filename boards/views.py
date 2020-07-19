from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from boards.models import List, Card
from boards.forms import ListForm


@login_required
def index(request):

    dictionary = {}
    lists = List.objects.filter(user_id=request.user.id)  #Filter lists by user_id

    for list in lists:
        cards = Card.objects.filter(list_id=list.id)
        dictionary[list.name] = cards

    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.user = request.user
            a.save()
            return redirect('index') #using GET request, for reloading the page without submitting form again
    else:
        form = ListForm()

    context = {'dictionary': dictionary, 'form': form}
    return render(request, 'boards/index.html', context)
# "lists" : { list1 : [card1, card2, car3] }