from django.db import models

class Usuario(models.Model):
    ADMIN = 'Admin'
    PORTEIRO = 'Porteiro'
    MORADOR = 'Morador'
    VISITANTE = 'Visitante'

    TIPO_USUARIO_CHOICES = [
        (ADMIN, 'Administrador'),
        (PORTEIRO, 'Porteiro'),
        (MORADOR, 'Morador'),
        (VISITANTE, 'Visitante'),
    ]

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    tipo_usuario = models.CharField(
        max_length=10,
        choices=TIPO_USUARIO_CHOICES,
        default=VISITANTE,
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    
class Visitante(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=10)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    
class RegistroDeAcesso(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    visitante = models.ForeignKey(Visitante, on_delete=models.CASCADE)
    data_hora_entrada = models.DateTimeField(auto_now_add=True)
    data_hora_saida = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.usuario.nome} - {self.visitante.nome}'