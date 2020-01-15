from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from emprestimo.models import Emprestimo

class EmprestimoSerializer(ModelSerializer):
    
    class Meta:
        model = Emprestimo
        fields = ('livros', 'usuario', 'data', 'data_devolucao', 'valor_multa')