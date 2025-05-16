from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone

TIPO_CONTA_CHOICES = (
    ('cidadao', 'Cidadão'),
    ('governo', 'Governo'),
    ('admin', 'Administrador')
)

class UsuarioManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email é obrigatório')
        email = self.normalize_email(email)
        if 'tipo_conta' not in extra_fields:
            extra_fields['tipo_conta'] = 'cidadao'
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('tipo_conta', 'admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuário precisa ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuário precisa ter is_superuser=True.')
        if extra_fields.get('tipo_conta') != 'admin':
            raise ValueError('Superusuário precisa ter tipo_conta=admin.')

        return self.create_user(username, email, password, **extra_fields)

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    tipo_conta = models.CharField(max_length=10, choices=TIPO_CONTA_CHOICES, default='cidadao')
    chave_acesso = models.CharField(max_length=100, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['email', 'cpf', 'tipo_conta']
    USERNAME_FIELD = 'username'

    objects = UsuarioManager()

    def __str__(self):
        return self.username
