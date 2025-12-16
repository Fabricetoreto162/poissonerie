from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


class InscriptionForm(UserCreationForm):
    email = forms.EmailField(label="Adresse e-mail")

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

        email = self.cleaned_data["email"]

        user.username = email   # 🔥 OBLIGATOIRE
        user.email = email

        if commit:
            user.save()
        return user



class ConnexionForm(forms.Form):
    email = forms.EmailField(label="Adresse e-mail")
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput
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
