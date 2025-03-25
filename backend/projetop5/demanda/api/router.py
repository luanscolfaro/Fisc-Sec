from rest_framework.routers import DefaultRouter,SimpleRouter
from demanda.api.viewsets import ReclamacaoViewSet 

router = SimpleRouter()
router.register(r'reclamacoes', ReclamacaoViewSet, basename='reclamacao')
