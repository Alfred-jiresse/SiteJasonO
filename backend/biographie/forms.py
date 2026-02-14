from django import forms
from .models import Auteur

class AuteurForm(forms.ModelForm):
    class Meta:
        model = Auteur
        fields = ['prenom', 'nom', 'biographie', 'photo']
        widgets = {
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'biographie': forms.Textarea(attrs={'rows': 4, 'cols': 20, 'class': 'form-control'}),
        }