from django.db import models

class Video(models.Model):
    titre = models.CharField(max_length=200)
    url = models.URLField(null=True, blank=True)
    description = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    fichier = models.FileField(upload_to='videos_fichiers/', blank=True, null=True)

    def __str__(self):
        return self.titre