from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializers import UsuarioSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    
    def create(self, request, *args, **kwargs):
        User.objects.create_user(request.data['username'], request.data['email'], request.data['password'], **kwargs)
        return Response({'Hello': request.data['username']})