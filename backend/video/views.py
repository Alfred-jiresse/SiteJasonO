from django.shortcuts import render
from .models import Video
from .forms import VideoForm
from django.contrib import messages

def video_list(request):
    videos = Video.objects.all().order_by('-date_publication')
    return render(request, 'liste_video.html', {'videos': videos})

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