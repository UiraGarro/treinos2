from rest_framework import serializers
from .models import Usuario, Visitante, AccessLog, Policial, PresencaDiaria, PolicialPresenca
from django.utils import timezone

class PolicialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Policial
        fields = ['id', 'nome', 'cpf', 'criado_em', 'atualizado_em']

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
        read_only_fields = ['horario_criacao', 'horario_entrada', 'horario_saida']
        extra_kwargs = {
            'visitante': {'required': True},
            'registrado_por': {'required': True}
        }

class PresencaDiariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresencaDiaria
        fields = ['id', 'policial', 'data']
        
class PolicialPresencaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicialPresenca
        
        fields = ['id', 'policial', 'horario_entrada', 'horario_saida']
        read_only_fields = ['horario_entrada']

class PolicialPresencaCheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicialPresenca
        fields = ['id', 'policial']
        read_only_fields = ['horario_entrada']
        extra_kwargs = {
            'policial': {'required': True}
        } 
    def create(self, validated_data):
        instance = PolicialPresenca.objects.create(**validated_data)
        instance.horario_entrada = timezone.now()
        instance.save()
        return instance
    
class PolicialPresencaCheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicialPresenca
        
        fields = ['id', 'policial']
        read_only_fields = ['horario_saida']
        extra_kwargs = {
            'policial': {'required': True}
        }
    def update(self, instance, validated_data):
        instance.horario_saida = timezone.now()
        instance.save()
        return instance
    def validate(self, data):
        if 'horario_saida' in data and not data['horario_saida']:
            raise serializers.ValidationError("Horário de saída não pode ser vazio.")
        return data
    def validate_policial(self, value):
        if not Policial.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Policial não encontrado.")
        return value
    def validate_horario_saida(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Horário de saída não pode ser no passado.")
        return value
    
class PolicialPresencaListSerializer(serializers.ModelSerializer):
    policial = PolicialSerializer()
    class Meta:
        model = PolicialPresenca
        fields = ['id', 'policial', 'horario_entrada', 'horario_saida']
        read_only_fields = ['horario_entrada', 'horario_saida']
        extra_kwargs = {
            'policial': {'required': True}
        }
    def validate(self, data):
        if 'horario_saida' in data and not data['horario_saida']:
            raise serializers.ValidationError("Horário de saída não pode ser vazio.")
        return data
    def validate_policial(self, value):
        if not Policial.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Policial não encontrado.")
        return value
    def validate_horario_saida(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Horário de saída não pode ser no passado.")
        return value
    def create(self, validated_data):
        instance = PolicialPresenca.objects.create(**validated_data)
        instance.horario_entrada = timezone.now()
        instance.save()
        return instance
    
