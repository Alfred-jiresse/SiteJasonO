from django.db import models

class Video(models.Model):
    titre = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre