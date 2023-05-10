from django.urls import path
from . import views
from .views import CategoryAPIView
urlpatterns =[
    path('',views.index,name='index'),
    path('listProd/',views.listProd,name='listProd'),
    path('listfour/',views.listfour,name='listfour'),
    path('listcom/',views.listcom,name='listcom'),
    path('addCommande/',views.addCommande,name='addCommande'),
    path('addprod/',views.addprod,name='addprod'),
    path('addForm/',views.addForm,name='addForm'),
    path('register/',views.register, name = 'register'),
    path('edit_product/',views.edit_product,name='edit_product'),
    path('post/edit/<int:id>/', views.edit_product, name='post-edit'),
    path('deletepersonnel/delete/<int:pk>/', views.deleteProduit, name='delete-produit'),
   path('editFourni/edit/<int:id>/', views.edit_Fourni, name='edit-fourni'),
    path('deletefournisseur/delete/<int:pk>/', views.deletefour, name='delete-four'),

         path('api/category/', CategoryAPIView.as_view())
]


