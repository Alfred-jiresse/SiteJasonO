"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contact.views import contact_view
from video.views import video_list, add_video
from livre.views import liste_livre, add_livre
from biographie.views import Auteur_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('biographie/modifier/', Auteur_view, name='modifier_biographie'),
    path('videos/', video_list, name='liste_video'),
    path('videos/ajouter/', add_video, name='ajouter_video'),
    path('livres/', liste_livre, name='liste_livre'),
    path('livres/ajouter/', add_livre, name='ajouter_livre'),
    path('contact/', contact_view, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
