from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from boards.models import List, Card
from boards.forms import ListForm, CardForm, ChangeListName

from django.http import JsonResponse
from django.core import serializers


@login_required
def index(request):

    dictionary = {}
    lists = List.objects.filter(user_id=request.user.id)  #Filter lists by user_id
    for list in lists:
        cards = Card.objects.filter(list_id=list.id)
        dictionary[list] = cards

    if request.method == 'POST':
        if request.POST.get("add-list") == "Add List":
            form_list = ListForm(request.POST)
            if form_list.is_valid():
                a = form_list.save(commit=False)
                a.user = request.user
                a.save()
                return redirect('index')

        if request.POST.get("add-card") == "Add Card":
            form_card = CardForm(request.POST)
            if form_card.is_valid():
                a = form_card.save(commit=False)
                a.user = request.user
                a.save()
                return redirect('index')  # using GET request, for reloading the page without submitting form again

        if request.POST.get("change-list-name") == "Change list name":
            if request.is_ajax:
                changeListName = ChangeListName(request.POST)
                if changeListName.is_valid():
                    a = List.objects.get(pk=1)
                    f = ChangeListName(request.POST, instance=a)
                    instance = f.save()
                    ser_instance = serializers.serialize('json', [instance, ])
                    return JsonResponse({"instance": ser_instance}, status=200)
                else:
                    return JsonResponse({"error": form.errors}, status=400)



    else:
        form_list = ListForm()
        form_card = CardForm()
        form_change_list_name = ChangeListName()

    forms_dict = {'form_list': form_list, 'form_card': form_card, 'form_change_list_name': form_change_list_name}
    context = {'dictionary': dictionary, 'form': forms_dict} # dictionary == "lists" : { list1 : [card1, card2, car3] }
    return render(request, 'boards/index.html', context)
