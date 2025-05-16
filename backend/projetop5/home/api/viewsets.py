from rest_framework.viewsets import ModelViewSet
from home.models import PaginaInicial
from home.api.serializers import PaginaInicialSerializer

class PaginaInicialViewSet(ModelViewSet):
    queryset = PaginaInicial.objects.filter(deleted_at__isnull=True, is_active=True)
    serializer_class = PaginaInicialSerializer
