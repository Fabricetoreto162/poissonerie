from stock.models import Carton, Notification

def verifier_stock_faible(produit, boutique=None):
    cartons_restants = Carton.objects.filter(
        produit=produit,
        boutique=boutique
    ).count()

    if cartons_restants <= produit.seuil_min_cartons:
        if not Notification.objects.filter(
            produit=produit,
            type_notification="STOCK_FAIBLE",
            active=True
        ).exists():
            Notification.objects.create(
                titre="Stock faible",
                message=(
                    f"Stock faible pour {produit.nom} : "
                    f"{cartons_restants} carton(s) restant(s)"
                ),
                type_notification="STOCK_FAIBLE",
                produit=produit,
                boutique=boutique
            )
