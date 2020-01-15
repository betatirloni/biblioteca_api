from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from livro.models import Livro

class LivroSerializer(ModelSerializer):
    
    class Meta:
        model = Livro
        fields = ('titulo', 'subtitulo', 'autores', 'foto', 'editora', 'numero_paginas')