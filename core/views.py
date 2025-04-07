from rest_framework import viewsets
from .models import Visitante, AccessLog, Policial, PresencaDiaria, PolicialPresenca
from .serializers import VisitanteSerializer, AccessLogSerializer, PolicialSerializer, PresencaDiariaSerializer, PolicialPresencaSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Visitante
from django.utils import timezone

class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitante.objects.all()
    serializer_class = VisitanteSerializer
    
    def perform_create(self, serializer):
        visitante = serializer.save()
        AccessLog.objects.create(visitante=visitante, acao='Criado', registrado_por=self.request.user)
    
class AccessLogViewSet(viewsets.ModelViewSet):
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer
    permission_classes = [IsAuthenticated]
    
class PolicialViewSet(viewsets.ModelViewSet):
    queryset = Policial.objects.all()
    serializer_class = PolicialSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        policial = serializer.save()
        AccessLog.objects.create(visitante=policial, acao='Criado', registrado_por=self.request.user)
class PresencaDiariaViewSet(viewsets.ModelViewSet):
    queryset = PresencaDiaria.objects.all()
    serializer_class = PresencaDiariaSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        presenca_diaria = serializer.save()
        AccessLog.objects.create(visitante=presenca_diaria.policial, acao='Criado', registrado_por=self.request.user)
class PolicialPresencaViewSet(viewsets.ModelViewSet):
    queryset = PolicialPresenca.objects.all()
    serializer_class = PolicialPresencaSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        policial_presenca = serializer.save()
        AccessLog.objects.create(visitante=policial_presenca.policial, acao='Criado', registrado_por=self.request.user)
    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.horario_saida:
            AccessLog.objects.create(visitante=instance.policial, acao='Saída', registrado_por=self.request.user)
        else:
            AccessLog.objects.create(visitante=instance.policial, acao='Entrada', registrado_por=self.request.user) 
    def perform_destroy(self, instance):
        AccessLog.objects.create(visitante=instance.policial, acao='Deletado', registrado_por=self.request.user)
        instance.delete()
class PolicialPresencaCheckInViewSet(viewsets.ModelViewSet):
    queryset = PolicialPresenca.objects.all()
    serializer_class = PolicialPresencaSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.horario_entrada = timezone.now()
        instance.save()
        AccessLog.objects.create(visitante=instance.policial, acao='Check-in', registrado_por=self.request.user)
        return instance
    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.horario_saida:
            AccessLog.objects.create(visitante=instance.policial, acao='Check-out', registrado_por=self.request.user)
        else:
            AccessLog.objects.create(visitante=instance.policial, acao='Check-in', registrado_por=self.request.user)
    def perform_destroy(self, instance):
        AccessLog.objects.create(visitante=instance.policial, acao='Deletado', registrado_por=self.request.user)
        instance.delete()
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(policial=self.request.user)
        return queryset
    def perform_destroy(self, instance):
        AccessLog.objects.create(visitante=instance.policial, acao='Deletado', registrado_por=self.request.user)
        instance.delete()
    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.horario_saida:
            AccessLog.objects.create(visitante=instance.policial, acao='Check-out', registrado_por=self.request.user)
        else:
            AccessLog.objects.create(visitante=instance.policial, acao='Check-in', registrado_por=self.request.user)
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.horario_entrada = timezone.now()
        instance.save()
        AccessLog.objects.create(visitante=instance.policial, acao='Check-in', registrado_por=self.request.user)

class PolicialPresencaCheckOutViewSet(viewsets.ModelViewSet):
    queryset = PolicialPresenca.objects.all()
    serializer_class = PolicialPresencaSerializer
    permission_classes = [IsAuthenticated]
    def perform_update(self, serializer):
        instance = serializer.save()
        instance.horario_saida = timezone.now()
        instance.save()
        AccessLog.objects.create(visitante=instance.policial, acao='Check-out', registrado_por=self.request.user)
        return instance
    def perform_destroy(self, instance):
        AccessLog.objects.create(visitante=instance.policial, acao='Deletado', registrado_por=self.request.user)
        instance.delete()
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(policial=self.request.user)
        return queryset
    def perform_destroy(self, instance):
        AccessLog.objects.create(visitante=instance.policial, acao='Deletado', registrado_por=self.request.user)
        instance.delete()
    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.horario_saida:
            AccessLog.objects.create(visitante=instance.policial, acao='Check-out', registrado_por=self.request.user)
        else:
            AccessLog.objects.create(visitante=instance.policial, acao='Check-in', registrado_por=self.request.user)
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.horario_entrada = timezone.now()
        instance.save()
        AccessLog.objects.create(visitante=instance.policial, acao='Check-in', registrado_por=self.request.user)
        return instance
    
