from django.shortcuts import render
from .models import Auteur
from .forms import AuteurForm
from django.contrib import messages

def auteur_view(request):
    auteurs = Auteur.objects.first()  # Récupère le premier auteur de la base de données
    if request.method == 'POST':
        form = AuteurForm(request.POST, request.FILES, instance=auteurs)
        if form.is_valid():
            form.save()
            messages.success(request, "La biographie a été mise à jour avec succès !")
    else:
        form = AuteurForm(instance=auteurs)

    return render(request, 'auteur.html', {'form': form, 'auteur': auteurs})

def biographie_view(request):
    is_auteur = request.user.is_authenticated and request.user.groups.filter(name='Auteur').exists()
    
    auteur = Auteur.objects.first()  # Récupère le premier auteur de la base de données
    context = {
        'auteur': auteur,
        'is_auteur': is_auteur,
    }
    return render(request, 'biographie.html', context)

def accueil_view(request):
    return render(request, 'index.html')