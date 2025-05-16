from rest_framework.viewsets import ModelViewSet
from demanda.models import Reclamacao
from demanda.api.serializers import ReclamacaoSerializer
from demanda.permissions import IsAdmin, IsGoverno, IsUsuario
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class ReclamacaoViewSet(ModelViewSet):
    serializer_class = ReclamacaoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:  # Admin vê tudo
            return Reclamacao.objects.all()
        elif user.tipo_conta == 'governo':  # Governo vê só as demandas para responder
            return Reclamacao.objects.filter(status__in=['pendente', 'em_resposta'])
        else:  # Usuário vê só as demandas que criou
            return Reclamacao.objects.filter(usuario=user)

    def perform_create(self, serializer):
        # vincula a reclamação ao usuário que criou
        serializer.save(usuario=self.request.user)

    def update(self, request, *args, **kwargs):
        user = request.user
        if user.tipo_conta == 'cidadao':
            return Response({"detail": "Usuário comum não pode alterar demandas."}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)
