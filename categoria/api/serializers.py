from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from categoria.models import Categoria

class CategoriaSerializer(ModelSerializer):
    
    class Meta:
        model = Categoria
        fields = ('nome', )