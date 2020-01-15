from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from autor.models import Autor

class AutorSerializer(ModelSerializer):
    
    class Meta:
        model = Autor
        fields = ('nome',)