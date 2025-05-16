from rest_framework import serializers
from home.models import PaginaInicial

class PaginaInicialSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaginaInicial
        fields = '__all__'
