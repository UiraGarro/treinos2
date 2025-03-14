from rest_framework import viewsets
from .models import Visitante, AccessLog
from .serializers import VisitanteSerializer, AccessLogSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Visitante
from rest_framework import status



class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitante.objects.all()
    serializer_class = VisitanteSerializer
    if status.code==200:
    
class AccessLogViewSet(viewsets.ModelViewSet):
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer
    permission_classes = [IsAuthenticated]
