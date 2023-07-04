from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome= models.TextField(max_length=255)
    cpf = models.CharField(max_length=11, default='00000000000')
    email = models.EmailField(max_length=50, default='Valor padrão')
    telefone = models.CharField(max_length=10, default='Valor padrão') # format: (12) 34567-8901
    endereco = models.CharField(max_length=200, default='Valor padrão')

    