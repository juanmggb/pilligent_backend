from rest_framework import serializers
from .models import Actuador

class ActuadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actuador
        fields = '__all__'
        
class ListaActuadoresSerializer(serializers.Serializer):
    actuadores = ActuadorSerializer(many=True)