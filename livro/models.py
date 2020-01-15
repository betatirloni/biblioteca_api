from django.db import models
from autor.models import Autor
from categoria.models import Categoria

class Livro(models.Model):
    
    titulo = models.CharField(max_length = 150)
    subtitulo = models.CharField(max_length = 150)
    autores = models.ManyToManyField(Autor)
    data_publicacao = models.DateField()
    descricao = models.TextField()
    numero_paginas = models.IntegerField()
    categoria = models.ManyToManyField(Categoria)
    disponivel = models.BooleanField(default=True)
    foto = models.ImageField(null=True, blank=True)
    editora = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.titulo
