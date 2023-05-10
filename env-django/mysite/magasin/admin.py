from django.contrib import admin
from .models import produit
admin.site.register(produit)
from .models import categorie
admin.site.register(categorie)
from .models import fournisseur
admin.site.register(fournisseur)
from .models import ProduitNC
admin.site.register(ProduitNC)
from .models import Commande
admin.site.register(Commande)
# Register your models here.
