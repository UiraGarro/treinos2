from rest_framework import serializers
from .models import Usuario, Visitante, AccessLog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'tipo_usuario']
        
class VisitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitante
        fields = '__all__'
        
class AccessLogSerializer(serializers.ModelSerializer):
    visitante = VisitanteSerializer()
    registrado_por = UserSerializer()
    
    class Meta:
        model = AccessLog
        fields = '__all__'