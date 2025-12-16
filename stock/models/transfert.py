from django.db import models
from .carton import Carton
from .boutique import Boutique


class Transfert(models.Model):
    carton = models.ForeignKey(Carton, on_delete=models.CASCADE)
    boutique_source = models.ForeignKey(Boutique, related_name='source', on_delete=models.CASCADE)
    boutique_destination = models.ForeignKey(Boutique, related_name='destination', on_delete=models.CASCADE)
    date_transfert = models.DateField(auto_now_add=True)