from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import InscriptionForm, ConnexionForm
from django.contrib.auth.decorators import login_required
from .models import Boutique, Categorie, Produit, Carton, Vente, Transfert, Mouvement
from .forms import BoutiqueForm
from .forms import CategorieForm
from .forms import ProduitForm
from .forms import CartonForm
from .forms import VenteForm
from .forms import TransfertForm
from .forms import MouvementForm






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


@login_required
def index(request):
    return render(request, 'Dashboard/index.html')





@login_required
def boutiques(request):
    boutiques = Boutique.objects.all()
    total_boutiques = Boutique.objects.count()

    if request.method == "POST":
        form = BoutiqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("boutiques")
    else:
        form = BoutiqueForm()

    return render(request, "Boutiques/boutiques.html", {
        "form": form,
        "boutiques": boutiques,
        "total_boutiques": total_boutiques
    })


@login_required
def categories(request):
    categories = Categorie.objects.all()

    if request.method == "POST":
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categories")
    else:
        form = CategorieForm()

    return render(request, "Categories/categories.html", {
        "form": form,
        "categories": categories
    })



@login_required
def produits(request):  
    produits = Produit.objects.all()

    if request.method == "POST":
            form =  ProduitForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("produits")
    else:
            form = CategorieForm()
    return render(request, 'Produits/produits.html', {'produits': produits})



@login_required
def cartons(request):
    cartons = Carton.objects.all()

    if request.method == "POST":
            form =  CartonForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("produits")
    else:
            form = CartonForm()
    return render(request, 'Cartons/cartons.html', {'cartons': cartons}) 





@login_required
def ventes(request):
    ventes = Vente.objects.all()

    if request.method == "POST":
            form =  VenteForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("produits")
    else:
            form = VenteForm()
    return render(request, 'Ventes/ventes.html', {'ventes': ventes})  



@login_required
def transferts(request):
    transferts = Transfert.objects.all()

    if request.method == "POST":
            form =  TransfertForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("produits")
    else:
            form = TransfertForm()
    return render(request, 'Transferts/transferts.html', {'transferts': transferts})




@login_required
def mouvements(request):
    mouvements = Mouvement.objects.all()

    if request.method == "POST":
            form =  MouvementForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("produits")
    else:
            form = MouvementForm()

    return render(request, 'Mouvements/mouvements.html', {'mouvements': mouvements})  


