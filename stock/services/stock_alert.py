# stock/services/stock_alert.py
from stock.models import Carton, Notification

def verifier_stock_faible(produit, boutique):

    cartons_restants = Carton.objects.filter(
        produit=produit,
        boutique=boutique,
        poids_restant__gt=0   # 👈 essentiel chez toi
    )

    nb_cartons = cartons_restants.count()

    notification = Notification.objects.filter(
        produit=produit,
        boutique=boutique,
        type_notification="STOCK_FAIBLE",
        active=True
    ).first()

    if nb_cartons == 2 and not notification:
        details = ", ".join(
            f"{produit.nom} {c.poids_restant}kg"
            for c in cartons_restants
        )

        Notification.objects.create(
            produit=produit,
            boutique=boutique,
            titre=f"Stock faible : {produit.nom}",
            message=f"Il reste 2 cartons : {details}",
            type_notification="STOCK_FAIBLE",
            active=True
        )

    elif nb_cartons > 2 and notification:
        notification.active = False
        notification.save()
