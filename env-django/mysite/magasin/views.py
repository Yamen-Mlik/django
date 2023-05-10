from sre_parse import CATEGORIES
from django.shortcuts import get_object_or_404, loader, redirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.urls import reverse_lazy
from .models import produit
from .forms import FournisseurForm, ProduitForm ,UserRegistrationForm,CommandeForm
from .models import produit
from .models import fournisseur,Commande
def listProd(request):
    products=produit.objects.all()
    context={'products':products}
    return render(request,'magasin/vitrine.html',context)
   
def addForm(request):
        if request.method == "POST":
            form = FournisseurForm(request.POST)
            if form.is_valid():
                form.save() 
                return redirect('listfour')
        else:   form = FournisseurForm() 
        return  render(request,'magasin/nouveauFournisseur.html',{'form':form})
def addprod(request):
    if request.method == "POST": 
        form = ProduitForm(request.POST)
        if form.is_valid():
             form.save() 
             return redirect('listProd')
    else : form = ProduitForm() 
    return render(request,'magasin/majProduits.html',{'form':form})
def listcom(request):
    cmds=Commande.objects.all()
    context={'cmds':cmds}
    return render(request,'magasin/lsc.html',context) 
def addCommande(request):
	if request.method == "POST":
		form = CommandeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('listcom')
	else:
		form=CommandeForm() 
	return  render(request,'magasin/addCommande.html',{'form':form})

def listfour(request):
    Fournis= fournisseur.objects.all()
    context={'Fournis':Fournis}
    return render(request,'magasin/mesFournisseur.html',context)
    # Create your views here.   """
def index(request): 
    return render(request,'magasin/vitrine.html')
def register(request):
    if request.method == 'POST' :
      form = UserRegistrationForm(request.POST)
      if form.is_valid():
       form.save()
       username = form.cleaned_data.get('username')
       password = form.cleaned_data.get('password1')
       user = authenticate(username=username, password=password)
    
      login(request,user)
      messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
      return redirect('home_page')
    else :
     form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form' : form})
def edit_product(request, id):
    post = get_object_or_404(produit, id=id)

    if request.method == 'GET':
        context = {'form': ProduitForm(instance=post), 'id': id}
        return render(request,'magasin/edit.html',context)
    elif request.method == 'POST':
        form = ProduitForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin/listProd/')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'magasin/edit.html',{'form':form})
def deleteProduit(request, pk):   
        produit.objects.filter(id=pk).delete()
        return HttpResponseRedirect('/magasin/listProd/')
 #Create your views here.
def edit_Fourni(request, id):
    post = get_object_or_404(fournisseur, id=id)

    if request.method == 'GET':
        context = {'form': FournisseurForm(instance=post), 'id': id}
        return render(request,'magasin/editfour.html',context)
    elif request.method == 'POST':
        form = FournisseurForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('listfour')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'magasin/edit_four.html',{'form':form})
def deletefour(request, pk):   
        fournisseur.objects.filter(id=pk).delete()
        return HttpResponseRedirect('/magasin/listfour/')



from rest_framework.views import APIView
from rest_framework.response import Response
 
from .models import categorie
from magasin.serializers import CategorySerializer
 
class CategoryAPIView(APIView):
 
    def get(self, *args, **kwargs):
        categories = categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
