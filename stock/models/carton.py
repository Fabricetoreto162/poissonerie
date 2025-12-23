from django.db import models
from .produit import Produit
from .boutique import Boutique


class Carton(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    poids_initial = models.FloatField()
    poids_restant = models.FloatField()
    boutique = models.ForeignKey(
        Boutique,
        on_delete=models.CASCADE,
        related_name="cartons"
    )
    date_entree = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Si création → poids_restant = poids_initial
        if self.pk is None:
            self.poids_restant = self.poids_initial
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.produit} - {self.poids_restant} kg restant"
