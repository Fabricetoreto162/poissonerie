from stock.models import Notification

def notifications_non_lues(request):
    if request.user.is_authenticated:
        return {
            "nb_notifications": Notification.objects.filter(
                lu=False,
                active=True
            ).count()
        }
    return {}
