from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password")
        labels = {
            "first_name": "Primeiro nome:",
            "last_name": "Sobrenome:",
            "username": "Nome de usuário:",
            "email": "E-mail:",
            "password": "Senha:",
        }
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Digite seu nome aqui"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Digite seu sobrenome aqui"}),
            "password": forms.PasswordInput(attrs={"placeholder": "Digite a sua senha aqui", "class": "senha"}),
        }
