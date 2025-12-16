from django.db import models
from .categorie import Categorie


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    prix_kg = models.IntegerField()


def __str__(self):
 return self.nom