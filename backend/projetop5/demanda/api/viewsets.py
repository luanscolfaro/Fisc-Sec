from rest_framework.viewsets import ModelViewSet
from demanda.models import Reclamacao
from demanda.api.serializers import ReclamacaoSerializer
from rest_framework import viewsets

class ReclamacaoViewSet(viewsets.ModelViewSet):
    queryset = Reclamacao.objects.all()
    serializer_class = ReclamacaoSerializer
