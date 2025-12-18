from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path("admin/",admin.site.urls),
    path('', views.inscription, name='inscription'),
    path('connexion/',views.connexion ,name='connexion'),
    path('deconnexion/',views.deconnexion ,name='deconnexion'),
    path('index/',views.index ,name='index'),
    path('boutiques/',views.boutiques ,name='boutiques'),
    path('categories/',views.categories ,name='categories'),
    path('produits/',views.produits ,name='produits'),
    path('cartons/',views.cartons ,name='cartons'),
    path('ventes/',views.ventes ,name='ventes'),
    path('transferts/',views.transferts ,name='transferts'),
    path('mouvements/',views.mouvements ,name='mouvements'),



]
