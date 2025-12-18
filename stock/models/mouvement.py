# stock/models/mouvement.py
from django.db import models
from .produit import Produit
from .carton import Carton
from .boutique import Boutique
from django.utils import timezone


class Mouvement(models.Model):

    TYPE_MOUVEMENT_CHOICES = (
        ("ENTREE", "Entrée"),
        ("SORTIE", "Sortie"),
    )

    type_mouvement = models.CharField(
        max_length=10,
        choices=TYPE_MOUVEMENT_CHOICES
    )

    produit = models.ForeignKey(
        Produit,
        on_delete=models.CASCADE
    )

    carton = models.ForeignKey(
        Carton,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    poids = models.FloatField(default=0)

    boutique = models.ForeignKey(
        "Boutique",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

  

    date_mouvement = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return f"{self.type_mouvement} - {self.produit} - {self.poids} kg"
