from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        max_length=254,
        label="E-mail:",
        widget=forms.EmailInput(attrs={"placeholder": "Digite seu e-mail aqui"})
        )
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

        validate_password(data)

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

        if password:
            user = User(
                first_name = cleaned_data.get("first_name") or "",
                last_name = cleaned_data.get("last_name") or "",
                username = cleaned_data.get("username") or "",
                email = cleaned_data.get("email") or "",
            )
            try:
                validate_password(password, user=user)
            except ValidationError as error:
                self.add_error("password", error)

        if password and confirm_password:
            if password != confirm_password:
                self.add_error("confirm_password", "As senhas não conhecidem 😕"),

        return cleaned_data

