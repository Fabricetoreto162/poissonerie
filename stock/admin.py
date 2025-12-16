from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Boutique)
admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Carton)
admin.site.register(Vente)
admin.site.register(Transfert)
admin.site.register(Mouvement)

