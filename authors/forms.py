from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(
        required=True,
        label="Repita a senha:",
        widget= forms.PasswordInput(attrs={"placeholder": "Repita sua senha aqui", "class": "senha"})
        )
    
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
        # error_messages = {
        #     "password": {
        #         "required": "Erro teste",
        #     },
        #}

    def clean_password(self):
        data = self.cleaned_data['password']

        if "teste" in data:
            raise ValidationError(
                "Não digite teste",
                code="invalid",
            )
            
        return data
    
    def clean_first_name(self):
        data = self.cleaned_data['first_name']

        if "Diogo" in data:
            raise ValidationError(
                "Diogo já está cadastrado e é único. Sorry 🤭😁",
                code="invalid",
            )
            
        return data

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                self.add_error("confirm_password", "As senhas não conhecidem 😕"),

        return cleaned_data

