from django.shortcuts import render
from .models import Video
from .forms import VideoForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

def is_auteur(user):
    return user.is_authenticated and user.groups.filter(name='Auteur').exists()

def video_list(request):
    is_auteur = request.user.is_authenticated and request.user.groups.filter(name='Auteur').exists()
    videos = Video.objects.all().order_by('-date_publication')
    context = {
        'videos': videos,
        'is_auteur': is_auteur,
    }
    return render(request, 'liste_video.html', context)

@user_passes_test(is_auteur)
def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "La vidéo a été ajoutée avec succès !")
            return redirect('liste_video')
    else:
        form = VideoForm()
    
    return render(request, 'videos.html', {'form': form})