from django.db import models
from .carton import Carton


class Vente(models.Model):
    carton = models.ForeignKey(Carton, on_delete=models.CASCADE)
    poids_vendu = models.FloatField()
    prix_total = models.IntegerField()
    date_vente = models.DateTimeField(auto_now_add=True)