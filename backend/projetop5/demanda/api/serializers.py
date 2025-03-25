from rest_framework.serializers import ModelSerializer
from demanda.models import Reclamacao

class ReclamacaoSerializer(ModelSerializer):
    class Meta:
        model = Reclamacao
        fields = '__all__'
