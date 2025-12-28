# stock/models/produit.py
from django.db import models
from .categorie import Categorie


class Produit(models.Model):
    nom = models.CharField(max_length=100)

    prix_kg = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="produits"
    )

    seuil_min_cartons = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.nom

