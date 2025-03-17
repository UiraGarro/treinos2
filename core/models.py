from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone

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


