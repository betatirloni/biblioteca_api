from rest_framework.viewsets import ModelViewSet
from autor.models import Autor
from .serializers import AutorSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer