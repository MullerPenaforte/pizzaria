from django import forms

class CadastroClienteForm(forms.Form):
    nome = forms.CharField(label='Nome Completo', max_length=100)
    cpf = forms.CharField(label='CPF', max_length=14) # format: 123.456.789-00
    email = forms.EmailField(label='E-mail')
    telefone = forms.CharField(label='Telefone', max_length=15) # format: (12) 34567-8901
    endereco = forms.CharField(label='Endereço', max_length=200)
