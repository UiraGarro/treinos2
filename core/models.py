from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone
from datetime import timedelta

class Usuario(AbstractUser):
    TIPO_USUARIO = (
        ('admin', 'Administrador'),
        ('portaria', 'Portaria'),
     )
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    groups = models.ManyToManyField(Group, related_name="usuario_groups")
    user_permissions = models.ManyToManyField(Permission, related_name="usuario_permissions")
    
    def __str__(self):
        return self.nome
    
    
class Visitante(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    
class AccessLog(models.Model):
    visitante = models.ForeignKey(Visitante, on_delete=models.CASCADE)
    registrado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    acao = models.CharField(max_length=100)
    horario_criação = models.DateTimeField(auto_now_add=True)
    horario_entrada = models.DateTimeField(null=True, blank=True)
    horario_saida = models.DateTimeField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.horario_entrada:
            self.horario_entrada = timezone.now()
        super().save(*args, **kwargs)
    
def __str__(self):
    return f"Registro de {self.visitante.nome} - {self.acao} - {self.horario_criacao}"

class Policial(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    
class PresencaDiaria(models.Model):
    policial = models.ForeignKey(Policial, on_delete=models.CASCADE)
    data = models.DateField()

    def __str__(self):
        return f"{self.policial.nome} - {self.data}"
        
class PolicialPresença(models.Model):
    policial = models.ForeignKey(Policial, on_delete=models.CASCADE)
    horario_entrada = models.DateTimeField(auto_now_add=True)
    horario_saida = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.horario_saida:
            self.horario_saida = timezone.now()
        super().save(*args, **kwargs)

    def check_in(self):
        if not self.horario_saida:
            self.horario_saida = timezone.now()
            self.save()
        # Registrar presença diária
        hoje = timezone.now().date()
        PresencaDiaria.objects.get_or_create(policial=self.policial, data=hoje)

    def check_out(self):
        if self.horario_saida:
            self.horario_saida = None

    def desertor(self):
        hoje = timezone.now().date()
        tres_dias_atras = hoje - timedelta(days=3)
        # Verificar se há registros de presença nos últimos 3 dias
        dias_presentes = PresencaDiaria.objects.filter(
            policial=self.policial,
            data__range=(tres_dias_atras, hoje)
        ).count()
        # Se não houve presença nos últimos 3 dias, é desertor
        if dias_presentes < 3:
            # Criar solicitação de prisão
            SolicitacaoPrisao.objects.get_or_create(policial=self.policial)
            return True
        return False

    def __str__(self):
        return f"{self.policial.nome} - {self.horario_entrada} a {self.horario_saida}"
    
class SolicitacaoPrisao(models.Model):
    visitante = models.ForeignKey(Visitante, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=255, default="Procurado")
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    policial = models.ForeignKey(Policial, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=255, default="Deserção")
    data_solicitacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitação de prisão para {self.policial.nome} - {self.motivo}"