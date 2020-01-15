from rest_framework.viewsets import ModelViewSet
from livro.models import Livro
from .serializers import LivroSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer