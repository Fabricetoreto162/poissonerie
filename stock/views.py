from django.shortcuts import render, redirect, get_object_or_404
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
def boutique_delete(request, pk):
    boutique = get_object_or_404(Boutique, pk=pk)

    if request.method == "POST":
        boutique.delete()
        return redirect("boutiques")

    return render(request, "Boutiques/boutiques.html", {
        "boutique": boutique
    })


@login_required
def boutique_update(request, pk):
    boutique = get_object_or_404(Boutique, pk=pk)

    if request.method == "POST":
        form = BoutiqueForm(request.POST, instance=boutique)
        if form.is_valid():
            form.save()
            return redirect("boutiques")
    else:
        form = BoutiqueForm(instance=boutique)

    return render(request, "Boutiques/boutiques.html", {
        "form": form,
        "boutique": boutique
    })







@login_required
def produits(request):
    categories = Categorie.objects.all()
    produits = Produit.objects.select_related("categorie")
    totales_produits= Produit.objects.count()

    # Gestion catégorie
    if request.method == "POST" and "add_categorie" in request.POST:
        categorie_form = CategorieForm(request.POST)
        produit_form = ProduitForm()
        if categorie_form.is_valid():
            categorie_form.save()
            return redirect("produits")

    # Gestion produit
    elif request.method == "POST" and "add_produit" in request.POST:
        produit_form = ProduitForm(request.POST)
        categorie_form = CategorieForm()
        if produit_form.is_valid():
            produit_form.save()
            return redirect("produits")

    else:
        categorie_form = CategorieForm()
        produit_form = ProduitForm()

    return render(request, "Produits/produits.html", {
        "categories": categories,
        "produits": produits,
        "categorie_form": categorie_form,
        "produit_form": produit_form,
        "totales_produits": totales_produits
    })


@login_required
def produits_update(request, pk):
    produit = get_object_or_404(Produit, pk=pk)

    if request.method == "POST":
        produit.nom = request.POST.get("nom")
        produit.prix_kg = request.POST.get("prix_kg")
        produit.categorie_id = request.POST.get("categorie")
        produit.save()
        return redirect("produits")

    return render(request, "Produits/produits.html", {
        "produit": produit,
        "categories": Categorie.objects.all()
    })


@login_required
def produits_delete(request, pk):
    produit = get_object_or_404(Produit, pk=pk)

    if request.method == "POST":
        produit.delete()
        return redirect("produits")

    return render(request, "Produits/produits.html", {
        "produit": produit
    })

@login_required
def categories_update(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)

    if request.method == "POST":
        categorie.nom = request.POST.get("nom")
        categorie.save()
        return redirect("produits")


@login_required
def categories_delete(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)

    if request.method == "POST":
        categorie.delete()
        return redirect("produits")



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


