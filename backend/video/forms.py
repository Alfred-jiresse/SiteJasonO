from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['titre', 'url', 'description', 'date_publication']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 20, 'class': 'form-control'}),
            'date_publication': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }