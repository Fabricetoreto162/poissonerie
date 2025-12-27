# stock/models/notification.py
from django.db import models
from django.utils import timezone
from .produit import Produit
from .boutique import Boutique

class Notification(models.Model):
    TYPE_CHOICES = (
        ("STOCK_FAIBLE", "Stock faible"),
        ("AJOUT", "Ajout"),
        ("MODIFICATION", "Modification"),
        ("SUPPRESSION", "Suppression"),
    )

    produit = models.ForeignKey(
        Produit,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    boutique = models.ForeignKey(
        Boutique,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    titre = models.CharField(max_length=255)
    message = models.TextField()
    type_notification = models.CharField(max_length=20, choices=TYPE_CHOICES)

    lu = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.titre
