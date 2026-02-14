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

    return render(request, 'biographie.html', {'form': form, 'auteur': auteurs})