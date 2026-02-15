from django import forms
from .models import Livre

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre', 'auteur', 'description', 'couverture', 'isbn', 'fichier', 'prix', 'devise']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'auteur': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 20, 'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'fichier': forms.FileInput(attrs={'class': 'form-control'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control'}),
            'devise': forms.TextInput(attrs={'class': 'form-control'}),
        }