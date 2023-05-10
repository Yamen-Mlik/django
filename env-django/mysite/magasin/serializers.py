from rest_framework.serializers import ModelSerializer
 
from .models import categorie
 
class CategorySerializer(ModelSerializer):
 
    class Meta:
        model = categorie
        fields = ['id', 'name']
