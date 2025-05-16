from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from usuario.models import Usuario
from usuario.forms import UsuarioCreateForm, UsuarioChangeForm

class CustomUsuarioAdmin(UserAdmin):
    model = Usuario
    add_form = UsuarioCreateForm
    form = UsuarioChangeForm

    list_display = ('username', 'email', 'cpf', 'tipo_conta', 'is_staff')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Informações Pessoais', {'fields': ('telefone', 'cpf')}),
        ('Permissões', {'fields': ('is_active', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'cpf', 'telefone', 'password1', 'password2'),
        }),
    )

    search_fields = ('username', 'email', 'cpf')
    ordering = ('username',)

    def get_fieldsets(self, request, obj=None):
        """Mostrar tipo_conta e campos staff/superuser só para superuser"""
        fieldsets = super().get_fieldsets(request, obj)
        if request.user.is_superuser:
            # adiciona tipo_conta e campos de permissão
            fieldsets = (
                (None, {'fields': ('username', 'email', 'password')}),
                ('Informações Pessoais', {'fields': ('telefone', 'cpf', 'tipo_conta')}),
                ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
                ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
            )
        return fieldsets

    def get_add_fieldsets(self, request):
        """Mostrar tipo_conta e campos staff/superuser só para superuser no add"""
        if request.user.is_superuser:
            return (
                (None, {
                    'classes': ('wide',),
                    'fields': ('username', 'email', 'cpf', 'telefone', 'tipo_conta', 'password1', 'password2', 'is_staff', 'is_superuser'),
                }),
            )
        return (
            (None, {
                'classes': ('wide',),
                'fields': ('username', 'email', 'cpf', 'telefone', 'password1', 'password2'),
            }),
        )

    def get_readonly_fields(self, request, obj=None):
        """Deixa tipo_conta readonly para não superuser"""
        if not request.user.is_superuser:
            return ('tipo_conta',)
        return super().get_readonly_fields(request, obj)

admin.site.register(Usuario, CustomUsuarioAdmin)
