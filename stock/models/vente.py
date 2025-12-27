# stock/models/vente.py
from django.db import models
from .produit import Produit
from .carton import Carton
from .boutique import Boutique




class Vente(models.Model):
    produit = models.ForeignKey(
        Produit,
        on_delete=models.CASCADE,
        related_name="ventes"
    )

    carton = models.ForeignKey(
        Carton,
        on_delete=models.CASCADE,
        related_name="ventes"
    )

    poids_vendu = models.FloatField()

    prix_unitaire = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    boutique = models.ForeignKey(
        Boutique,
        on_delete=models.CASCADE,
        related_name="ventes"
    )

    date_vente = models.DateTimeField(auto_now_add=True)

   

    def __str__(self):
        return f"Vente {self.produit} - {self.poids_vendu} kg"
    

