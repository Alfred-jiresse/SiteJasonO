from django.db import models

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=100, default='Jason Ololo')
    description = models.TextField()
    couverture = models.ImageField(upload_to='livres_couvertures/')
    date_publication = models.DateTimeField(auto_now_add=True)
    isbn = models.CharField(max_length=20, unique=True)
    fichier = models.FileField(upload_to='livres_fichiers/', blank=True, null=True)
    prix = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    devise = models.CharField(max_length=10, default='USD')

    def __str__(self):
        return self.titre
