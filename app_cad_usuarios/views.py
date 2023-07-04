from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Usuario
# Create your views here.

def home(request):
    return render(request, 'usuarios/home.html')

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

def cardapio(request):
    return render(request, 'usuarios/cardapio.html')

def login(request):
    return render(request, 'usuarios/login.html')


def usuarios(request):
    # Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.cpf = request.POST.get('cpf')
    novo_usuario.save()

    #Exibir todos os usuarios ja cadastrados em um nova pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #Retornar os dados cadastros para 
    return render(request,'usuarios/usuarios.html', usuarios)