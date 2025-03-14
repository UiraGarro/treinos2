from rest_framework import viewsets
from .models import Visitante, AccessLog
from .serializers import VisitanteSerializer, AccessLogSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Visitante

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
