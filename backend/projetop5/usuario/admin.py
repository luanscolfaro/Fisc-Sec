from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from usuario.models import Usuario

class CustomUsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('username', 'email', 'cpf', 'tipo_conta', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('telefone', 'cpf', 'tipo_conta', 'chave_acesso')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('telefone', 'cpf', 'tipo_conta', 'chave_acesso')}),
    )

admin.site.register(Usuario, CustomUsuarioAdmin)
