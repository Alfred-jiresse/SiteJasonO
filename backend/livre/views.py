from django.shortcuts import render, redirect
from .models import Livre
from .forms import LivreForm
from django.contrib import messages

def liste_livre(request):
    livres = Livre.objects.all().order_by('isbn')
    return render(request, 'liste_livre.html', {'livres': livres})

def add_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Le livre a été ajouté avec succès !")
            return redirect('liste_livre')
    else:
        form = LivreForm()
    
    return render(request, 'livres.html', {'form': form})