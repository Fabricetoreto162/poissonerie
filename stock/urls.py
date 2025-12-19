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
    path("boutique/supprimer/<int:pk>/", views.boutique_delete, name="boutique_delete"),
    path("boutique/modifier/<int:pk>/", views.boutique_update, name="boutique_update"),
    path('produits/',views.produits ,name='produits'),
    path("categories/update/<int:pk>/", views.categories_update, name="categories_update"),
    path("categories/delete/<int:pk>/", views.categories_delete, name="categories_delete"),
    path("produits/update/<int:pk>/", views.produits_update, name="produits_update"),
    path("produits/delete/<int:pk>/", views.produits_delete, name="produits_delete"),
    path('cartons/',views.cartons ,name='cartons'),
    path('ventes/',views.ventes ,name='ventes'),
    path('transferts/',views.transferts ,name='transferts'),
    path('mouvements/',views.mouvements ,name='mouvements'),



]
