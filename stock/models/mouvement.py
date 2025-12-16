from django.db import models


class Mouvement(models.Model):
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)