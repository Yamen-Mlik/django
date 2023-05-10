from django import forms 
from django.forms import ModelForm
from .models import produit,fournisseur,Commande
class ProduitForm(ModelForm):
 class Meta :
  model = produit
  fields = "__all__" #pour tous les champs de la table
#fields=['libelle','description'] #pour qulques champs
class FournisseurForm(ModelForm):
    class Meta:
        model= fournisseur
        fields="__all__"
class Produitupdate(ModelForm):
    model = produit
    fields = "__all__" 
    template_name_suffix = '_update_form'
        
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class UserRegistrationForm(UserCreationForm):
  first_name = forms.CharField(label='Prénom')
  last_name = forms.CharField(label='Nom')
  email = forms.EmailField(label='Adresse e-mail')
class Meta(UserCreationForm.Meta):
 model = User
 fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')
class CommandeForm(ModelForm):
    class Meta:
        model= Commande
        fields="__all__"