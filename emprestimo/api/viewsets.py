from rest_framework.viewsets import ModelViewSet
from emprestimo.models import Emprestimo
from .serializers import EmprestimoSerializer

class EmprestimoViewSet(ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer