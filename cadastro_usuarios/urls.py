"""
URL configuration for cadastro_usuarios project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    #rota, view responsavel, nome de referencia
    # facebook.com
    path('',views.home, name = 'home'),
    # facebook.com/devaprender
    #usuario.com
    #usarios.com/usuarios
    path('usuarios/',views.usuarios, name='listagem_usuarios'),
    path('cardapio/',views.cardapio, name='cardapio'),
    path('cardapio2/',views.cardapio2, name='cardapio2'),
    path('login/',views.login, name='login'),
    path('cadastro/',views.cadastro, name='cadastro')
]
