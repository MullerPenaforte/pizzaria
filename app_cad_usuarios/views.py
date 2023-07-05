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

def cardapio2(request):
    from django.shortcuts import render

    
    is_authenticated = request.user.is_authenticated
    return render(request, 'usuarios/cardapio2.html', {'is_authenticated': is_authenticated})

    

def login(request):
    return render(request, 'usuarios/login.html')

def pedido(request):
    return render(request, 'usuarios/pedido.html')


def usuarios(request):
    # Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.endereco = request.POST.get('endereco')
    novo_usuario.telefone = request.POST.get('telefone')
    novo_usuario.save()

    #Exibir todos os usuarios ja cadastrados em um nova pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
        
    }
    #Retornar os dados cadastros para 
    return render(request,'usuarios/usuarios.html', usuarios)

from django.shortcuts import render

def cardapio2(request):
    is_logged_in = request.user.is_authenticated
    return render(request, 'usuarios/cardapio2.html', {'is_logged_in': is_logged_in})
