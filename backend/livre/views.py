from django.shortcuts import render, redirect
from .models import Livre
from .forms import LivreForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

def is_auteur(user):
    return user.is_authenticated and user.groups.filter(name='Auteur').exists()

def liste_livre(request):
    is_auteur = request.user.is_authenticated and request.user.groups.filter(name='Auteur').exists()
    livres = Livre.objects.all().order_by('isbn')
    context = {
        'livres': livres,
        'is_auteur': is_auteur,
    }
    return render(request, 'liste_livre.html', context)

@user_passes_test(is_auteur)
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

@user_passes_test(is_auteur)
def delete_livre(request, livre_id):
    livre = Livre.objects.get(id=livre_id)
    if request.method == 'POST':
        livre.delete()
        return redirect('liste_livre')
    return render(request, 'confirm_delete.html', {'livre': livre})