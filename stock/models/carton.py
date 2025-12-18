from django.db import models
from .produit import Produit
from .boutique import Boutique


class Carton(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    poids_initial = models.FloatField()
    poids_restant = models.FloatField()
    boutique = models.ForeignKey(Boutique, on_delete=models.CASCADE)
    date_entree = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.produit} - {self.poids_restant} kg"