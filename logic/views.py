#-*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render
from logic.forms import CallForm
from logic.mathplus.compiler import make
 
def home(request):
  return render(request, 'home.html', {'current_date': datetime.now()})

def doc(request):
  return render(request, 'doc.html', {'current_date': datetime.now()})
 
def example(request):
  return render(request, 'example.html', {'current_date': datetime.now()})
 
def fishing(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = CallForm(request.POST)  # Nous reprenons les données
 
        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
 
            # Ici nous pouvons traiter les données du formulaire
            author = form.cleaned_data['author']
            call = form.cleaned_data['call']
 	    dem = make(call)

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = CallForm()  # Nous créons un formulaire vide
 
    return render(request, 'fishing.html', locals())
