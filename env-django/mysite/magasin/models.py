import datetime
from sqlite3 import Date
from django.db import models

      
# Create your models here.
class produit(models.Model):
    TYPE_CHOICES=[
        ('em','emballé'),
        ('fr','Frais'),
        ('cs','Conserve')
    ]
    libelle=models.CharField(max_length=100)
    description=models.TextField(default='Non définie')
    prix=models.DecimalField(max_digits=10,decimal_places=3,default=0)
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img=models.ImageField(blank=True,upload_to='media/')
    categorie=models.ForeignKey('categorie',on_delete=models.CASCADE,null=True)
    fournisseur=models.ForeignKey('fournisseur',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.libelle+str(self.prix)+self.description+self.type
class ProduitNC(produit):
    Duree_garantie=models.CharField(max_length=100)
    def __str__(self):
            return self.Duree_garantie
class Commande(models.Model):
    dateCde=models.DateField(null=True,default=Date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits = models.ManyToManyField('produit')
    def __str__(self):
        return self.dateCde+self.totalCde+self.produits
class fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length=8)
    def __str__(self):
        return self.nom +self.adresse + self.email + self.telephone
class categorie(models.Model):
      TYPE_CHOICES=[
        ('Al','Alimentaire'),
        ('Mb','Meuble'),
        ('vs','vaisselle')
    ]
      libelle=models.CharField(default='Al',choices=TYPE_CHOICES,max_length=50)
      def __str__(self) -> str:
           return 'libellé : '+self.libelle
class user (models.Model):
     username = models.CharField(max_length=100)
     first_name = models.CharField(max_length=100)
     last_name = models.CharField(max_length=100)
     email = models.EmailField()
     def __str__(self):
          return self.username +self.first_name + self.last_name + self.email