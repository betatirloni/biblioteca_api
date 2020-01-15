"""biblioteca_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from livro.api.viewsets import LivroViewSet
from emprestimo.api.viewsets import EmprestimoViewSet
from autor.api.viewsets import AutorViewSet
from categoria.api.viewsets import CategoriaViewSet

routers = routers.DefaultRouter()
routers.register(r'livros', LivroViewSet)
routers.register(r'emprestimos', EmprestimoViewSet)
routers.register(r'autores', AutorViewSet)
routers.register(r'categorias', CategoriaViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
