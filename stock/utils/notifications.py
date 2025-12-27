from stock.models import Notification

def creer_notification(
    titre,
    message,
    type_notification,
    produit=None,
    boutique=None
):
    Notification.objects.create(
        titre=titre,
        message=message,
        type_notification=type_notification,
        produit=produit,
        boutique=boutique
    )






def notif_ajout(carton):
    Notification.objects.create(
        titre="Ajout de carton",
        message=f"Un nouveau carton de {carton.produit.nom} a été ajouté.",
        type_notification="AJOUT",
        produit=carton.produit,
        boutique=carton.boutique
    )


def notif_modification(carton):
    Notification.objects.create(
        titre="Modification de carton",
        message=f"Le carton de {carton.produit.nom} a été modifié.",
        type_notification="MODIFICATION",
        produit=carton.produit,
        boutique=carton.boutique
    )


def notif_suppression(carton):
    Notification.objects.create(
        titre="Suppression de carton",
        message=f"Le carton de {carton.produit.nom} a été supprimé.",
        type_notification="SUPPRESSION",
        produit=carton.produit,
        boutique=carton.boutique
    )
