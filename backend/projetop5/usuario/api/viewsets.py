from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied
from usuario.models import Usuario
from usuario.api.serializers import UsuarioSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        user = self.request.user
        if user.tipo_conta in ['governo', 'admin']:
            return Usuario.objects.all()
        else:
            # Usuário cidadão só vê a si mesmo
            return Usuario.objects.filter(id=user.id)

    def perform_create(self, serializer):
        user = self.request.user
        tipo_conta = serializer.validated_data.get('tipo_conta', 'cidadao')

        # Apenas admin pode definir tipo_conta diferente de cidadao
        if user.tipo_conta != 'admin' and tipo_conta != 'cidadao':
            raise PermissionDenied("Você não tem permissão para definir tipo de conta diferente de 'cidadao'.")
        
        serializer.save()

    def perform_update(self, serializer):
        user = self.request.user
        tipo_conta = serializer.validated_data.get('tipo_conta', None)

        # Apenas admin pode alterar tipo_conta para diferente de cidadao
        if tipo_conta and user.tipo_conta != 'admin' and tipo_conta != 'cidadao':
            raise PermissionDenied("Você não tem permissão para alterar tipo de conta para diferente de 'cidadao'.")
        
        serializer.save()
