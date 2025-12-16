from django.db import models


class Boutique(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255, blank=True)


def __str__(self):
    return self.nom