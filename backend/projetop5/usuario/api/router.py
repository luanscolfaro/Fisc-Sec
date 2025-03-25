from rest_framework.routers import DefaultRouter
from usuario.api.viewsets import UsuarioViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')

urlpatterns = [
    path('', include(router.urls)),
]
