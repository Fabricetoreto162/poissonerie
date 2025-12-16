from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import InscriptionForm, ConnexionForm

from .models import Boutique, Categorie, Produit, Carton, Vente, Transfert, Mouvement


def inscription(request):
    form = InscriptionForm()

    if request.method == "POST":
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("connexion")

    return render(request, "Auth/inscription.html", {
        "form": form
    })


def connexion(request):
    form = ConnexionForm()

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("index")

    return render(request, "Auth/connexion.html", {
        "form": form
    })


def deconnexion(request):
    logout(request)
    return redirect("connexion")



def index(request):
    return render(request, 'Dashboard/index.html')

def boutiques(request):
    boutiques = Boutique.objects.all()
    return render(request, 'Boutiques/boutiques.html', {'boutiques': boutiques})

def categories(request):
    categories = Categorie.objects.all()
    return render(request, 'Dashboard/categories.html', {'categories': categories})  

def produits(request):  
    produits = Produit.objects.all()
    return render(request, 'Produits/produits.html', {'produits': produits})

def cartons(request):
    cartons = Carton.objects.all()
    return render(request, 'Cartons/cartons.html', {'cartons': cartons})   

def ventes(request):
    ventes = Vente.objects.all()
    return render(request, 'Ventes/ventes.html', {'ventes': ventes})  

def transferts(request):
    transferts = Transfert.objects.all()
    return render(request, 'Transferts/transferts.html', {'transferts': transferts})

def mouvements(request):
    mouvements = Mouvement.objects.all()
    return render(request, 'Mouvements/mouvements.html', {'mouvements': mouvements})  


