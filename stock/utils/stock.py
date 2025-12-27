from stock.models import Carton
from stock.utils.notifications import creer_notification

def verifier_stock_faible(produit, boutique):
    nb_cartons = Carton.objects.filter(
        produit=produit,
        boutique=boutique,
        actif=True
    ).count()

    if nb_cartons <= produit.seuil_min_cartons:
        cartons = Carton.objects.filter(
            produit=produit,
            boutique=boutique,
            actif=True
        )

        details = ", ".join([
            f"{produit.nom} {c.poids}kg"
            for c in cartons
        ])

        creer_notification(
            titre="Stock faible",
            message=f"Il reste {nb_cartons} carton(s) : {details}",
            type_notification="STOCK_FAIBLE",
            produit=produit,
            boutique=boutique
        )
