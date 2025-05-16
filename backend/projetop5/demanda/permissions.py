from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser

class IsGoverno(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.tipo_conta == 'governo'

class IsUsuario(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.tipo_conta == 'cidadao'
