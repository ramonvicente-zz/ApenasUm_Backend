from django import forms
from allauth.account.forms import SignupForm

from .models import *

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome_completo', 'cpf', 'email', 'telefone', 'tipo_usuario', 'caixa', 'gerente', 'supervisor']

    def __init__(self,*args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)

        # GENERAL INFO
        self.fields['nome_completo'].widget.attrs['class'] = 'form-control'
        self.fields['nome_completo'].widget.attrs['placeholder'] = 'Nome Completo'

        self.fields['cpf'].widget.attrs['class'] = 'form-control masked-cpf'
        self.fields['cpf'].widget.attrs['placeholder'] = 'CPF'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

        self.fields['telefone'].widget.attrs['class'] = 'form-control masked-phone'
        self.fields['telefone'].widget.attrs['placeholder'] = 'Telefone'

        self.fields['tipo_usuario'].widget.attrs['class'] = 'form-control'

        self.fields['caixa'].widget.attrs['class'] = 'form-control'

        self.fields['gerente'].widget.attrs['class'] = 'form-control'
        self.fields['gerente'].queryset = Usuario.objects.filter(tipo_usuario='Gerente')

        self.fields['supervisor'].widget.attrs['class'] = 'form-control'
        self.fields['supervisor'].queryset = Usuario.objects.filter(tipo_usuario='Supervisor')
