from django.db import models

class Auteur(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=200)
    biographie = models.TextField()
    photo = models.ImageField(upload_to='auteurs_photos/')

    def __str__(self):
        return f"{self.prenom} {self.nom}"

