from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class UsuarioCreateForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'cpf', 'telefone', 'tipo_conta')  # removido chave_acesso

class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'cpf', 'telefone', 'tipo_conta', 'is_active', 'is_staff', 'is_superuser')
