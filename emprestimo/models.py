from django.db import models
from livro.models import Livro
from django.contrib.auth.models import User


class Emprestimo(models.Model):
    
    livros = models.ManyToManyField(Livro)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=True)
    data_devolucao = models.DateTimeField(null=True, blank=True)
    valor_multa = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.usuario.username