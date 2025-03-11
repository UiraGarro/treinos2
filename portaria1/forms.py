from django import forms
from .models import Usuario, Visitante, RegistroDeAcesso

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha', 'tipo_usuario']

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = ['nome', 'cpf', 'rg']

class RegistroDeAcessoForm(forms.ModelForm):
    class Meta:
        model = RegistroDeAcesso
        fields = ['usuario', 'visitante', 'data_hora_entrada', 'data_hora_saida']