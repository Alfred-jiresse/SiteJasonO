from django.db import models

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=100)
    description = models.TextField()
    couverture = models.ImageField(upload_to='livres_couvertures/')
    isbn = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.titre
