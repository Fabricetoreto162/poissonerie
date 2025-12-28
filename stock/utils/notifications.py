from django.utils import timezone
from stock.models import Notification, Carton


# ==============================
# 🔔 NOTIFICATION CARTON
# ==============================

def notif_ajout(carton):
    Notification.objects.create(
        titre="Nouveau carton ajouté",
        message=f"{carton.produit.nom} ({carton.poids_initial} kg)",
        type_notification="AJOUT",
        produit=carton.produit,
        boutique=carton.boutique,
        date=timezone.now()
    )


def notif_modification(carton):
    Notification.objects.create(
        titre="Carton modifié",
        message=f"{carton.produit.nom} mis à jour",
        type_notification="MODIFICATION",
        produit=carton.produit,
        boutique=carton.boutique,
        date=timezone.now()
    )


def notif_suppression(carton):
    Notification.objects.create(
        titre="Carton supprimé",
        message=f"{carton.produit.nom} supprimé",
        type_notification="SUPPRESSION",
        produit=carton.produit,
        boutique=carton.boutique,
        date=timezone.now()
    )

def notif_vente_suppression(vente):
    Notification.objects.create(
        titre="Vente supprimée",
        message=(
            f"Vente de {vente.poids_vendu} kg de "
            f"{vente.carton.produit.nom} supprimée"
        ),
        type_notification="SUPPRESSION",
        produit=vente.carton.produit,
        boutique=vente.carton.boutique,
        date=timezone.now()
    )