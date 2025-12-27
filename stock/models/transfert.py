# stock/models/transfert.py
from django.db import models
from .carton import Carton
from .boutique import Boutique



class Transfert(models.Model):
    carton = models.ForeignKey(
        Carton,
        on_delete=models.CASCADE,
        related_name="transferts"
    )
    

    boutique_source = models.ForeignKey(
        Boutique,
        on_delete=models.CASCADE,
        related_name="transferts_source"
    )
    

    boutique_destination = models.ForeignKey(
        Boutique,
        on_delete=models.CASCADE,
        related_name="transferts_destination"
    )

    date_transfert = models.DateTimeField(auto_now_add=True)
    



    def __str__(self):
        return f"Transfert {self.carton.id} : {self.boutique_source} → {self.boutique_destination}"
