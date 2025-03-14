from django.contrib import admin
from .models import Visitante, AccessLog

@admin.register(Visitante)
class VisitanteAdmin(admin.ModelAdmin):
    list_display =('id', 'nome', 'cpf', 'criado_em', 'atualizado_em')
    
@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_display =('visitante', 'registrado_por', 'horario_criação', 'horario_entrada', 'horario_saida')