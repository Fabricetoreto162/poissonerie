# stock/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from stock.models import Carton, Notification

@receiver(post_save, sender=Carton)
def notification_ajout_modification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            titre="Nouveau carton ajouté",
            message=f"Carton de {instance.produit.nom} ajouté ({instance.poids_initial} kg)",
            type_notification="AJOUT"
        )
    else:
        Notification.objects.create(
            titre="Carton modifié",
            message=f"{instance.produit.nom} modifié",
            type_notification="MODIFICATION"
        )


@receiver(post_delete, sender=Carton)
def notification_suppression(sender, instance, **kwargs):
    Notification.objects.create(
        titre="Carton supprimé",
        message=(
            f"Le carton de {instance.produit.nom} "
            f"({instance.poids_initial} kg) a été supprimé"
        ),

        type_notification="SUPPRESSION"
    )

