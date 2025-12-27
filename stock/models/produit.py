# stock/models/produit.py
from django.db import models
from .categorie import Categorie


class Produit(models.Model):
    nom = models.CharField(max_length=150)
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE,
        related_name="produits"
    )
    prix_kg = models.FloatField()

   

    def __str__(self):
        return self.nom
