from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from django.contrib.auth.models import User, UserManager

class UsuarioSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email', 'password')