from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models.boutique import Boutique
from .models.produit import Produit
from .models.carton import Carton
from .models.vente import Vente
from .models.transfert import Transfert
from .models.mouvement import Mouvement
from .models.categorie import Categorie


# ======================
# INSCRIPTION
# ======================
class InscriptionForm(UserCreationForm):
    email = forms.EmailField(
        label="Adresse e-mail",
        widget=forms.EmailInput(attrs={
            "class": "form-input",
            "placeholder": "Entrez votre email"
        })
    )

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet email existe déjà")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]  # 🔥 email = username
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user


# ======================
# CONNEXION (EMAIL)

class ConnexionForm(forms.Form):
    email = forms.EmailField(
        label="Adresse email",
        widget=forms.EmailInput(attrs={
            "class": "form-input",
            "placeholder": "Entrez votre email"
        })
    )

    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            "class": "form-input",
            "placeholder": "Entrez votre mot de passe"
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError("Email ou mot de passe incorrect")

        user = authenticate(username=user.username, password=password)
        if user is None:
            raise forms.ValidationError("Email ou mot de passe incorrect")

        self.user = user
        return cleaned_data

    def get_user(self):
        return self.user


class BoutiqueForm(forms.ModelForm):
    class Meta:
        model = Boutique
        fields = ["nom"]
        widgets = {
            "nom": forms.TextInput(attrs={"class": "form-control w-100", "placeholder": "Nom de la boutique"}),
            
            
        }



class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ["nom"]
        widgets = {
            "nom": forms.TextInput(attrs={
                "class": "form-control w-100",
                "placeholder": "Nom de la catégorie"
            })
        }


class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ["nom", "categorie", "prix_kg"]
        widgets = {
            "nom": forms.TextInput(attrs={"class": "form-input", "placeholder": "Nom du produit"}),
            "categorie": forms.Select(attrs={"class": "form-input","placeholder": "Sélecionner la categories"}),
            "prix_kg": forms.NumberInput(attrs={"class": "form-input", "placeholder": "Prix par kg"}),
        }






class CartonForm(forms.ModelForm):
    class Meta:
        model = Carton
        fields = [
            "produit",
            "poids_initial",
            "poids_restant",
            "boutique",
        ]
        widgets = {
            "produit": forms.Select(attrs={
                "class": "form-input"
            }),
            "poids_initial": forms.NumberInput(attrs={
                "class": "form-input",
                "placeholder": "Poids initial (kg)",
                "step": "0.01",
                "min": "0"
            }),
            "poids_restant": forms.NumberInput(attrs={
                "class": "form-input",
                "placeholder": "Poids restant (kg)",
                "step": "0.01",
                "min": "0"
            }),
            "boutique": forms.Select(attrs={
                "class": "form-input"
            }),
        }



class VenteForm(forms.ModelForm):
    class Meta:
        model = Vente
        fields = [
            "produit",
            "carton",
            "poids_vendu",
            "prix_unitaire",
            "boutique"
        ]
        widgets = {
            "produit": forms.Select(attrs={"class": "form-input"}),
            "carton": forms.Select(attrs={"class": "form-input"}),
            "poids_vendu": forms.NumberInput(attrs={"class": "form-input", "placeholder": "Poids vendu (kg)"}),
            "prix_unitaire": forms.NumberInput(attrs={"class": "form-input", "placeholder": "Prix unitaire"}),
            "boutique": forms.Select(attrs={"class": "form-input"}),
        }


class TransfertForm(forms.ModelForm):
    class Meta:
        model = Transfert
        fields = [
            "carton",
            "boutique_source",
            "boutique_destination"
        ]
        widgets = {
            "carton": forms.Select(attrs={"class": "form-input"}),
            "boutique_source": forms.Select(attrs={"class": "form-input"}),
            "boutique_destination": forms.Select(attrs={"class": "form-input"}),
        }



class MouvementForm(forms.ModelForm):
    class Meta:
        model = Mouvement
        fields = [
            "type_mouvement",
            "produit",
            "carton",
            "poids",
            "boutique"
        ]
        widgets = {
            "type_mouvement": forms.Select(attrs={"class": "form-input"}),
            "produit": forms.Select(attrs={"class": "form-input"}),
            "carton": forms.Select(attrs={"class": "form-input"}),
            "poids": forms.NumberInput(attrs={"class": "form-input", "placeholder": "Poids (kg)"}),
            "boutique": forms.Select(attrs={"class": "form-input"}),
        }














