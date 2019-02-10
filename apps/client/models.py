from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from apps.common.fields import JSONField
from apps.common.models import BestPraticesModel
from apps.core.models import Address, State, City
from django.db.models.signals import post_save

import re

class Usuario(BestPraticesModel):
    TIPO_USUARIO = (
        ('Gerente', 'Gerente'),
        ('Operador', 'Operador'),
        ('Supervisor', 'Supervisor'),
        ('Master', 'Master'),
    )
    # USER INFO
    tipo_usuario = models.CharField(verbose_name='Tipo Usuário', max_length=30, choices=TIPO_USUARIO)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    gerente = models.ForeignKey('self', null=True, blank=True, related_name='user_gerente', on_delete=models.SET_NULL)
    supervisor = models.ForeignKey('self', null=True, blank=True, related_name='user_supervisor', on_delete=models.SET_NULL)
    caixa = models.ForeignKey('CaixaSelect', verbose_name='Caixas', blank=True, null=True, on_delete=models.DO_NOTHING)
    # BASIC INFO
    nome_completo = models.CharField('Nome Completo', max_length=200)
    email = models.EmailField('Email', max_length=100)
    cpf = models.CharField('CPF', max_length=14, blank=True, null=True)
    telefone = models.CharField('Telefone', max_length=20, blank=True, null=True)
    # CONFIRMATION INFO
    sms_code = models.CharField(max_length=4, blank=True, null=True)
    sms_date = models.DateTimeField(blank=True, null=True)
    sms_resends = models.IntegerField(default=0, blank=True, null=True)
    confirmation_sms = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
    
    def __str__(self):
        return '{}'.format(self.nome_completo)


class Caixa(BestPraticesModel):
    descricao = models.CharField(verbose_name='Descrição', max_length=254)
    usuario_responsavel = models.ForeignKey(Usuario, verbose_name='Usuário Responsável', related_name='user_responsavel', blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Caixa"
        verbose_name_plural = "Caixas"
    
    def __str__(self):
        return '{}'.format(self.descricao)


def create_padrao(sender, instance, created, **kwargs):
	if created:
		caixa = CaixaSelect()
		caixa.caixa = instance
		caixa.save()

post_save.connect(create_padrao, sender=Caixa)


class CaixaSelect(BestPraticesModel):
    caixa = models.ForeignKey(Caixa, verbose_name='Caixas', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Caixa Cadastrado"
        verbose_name_plural = "Caixas Cadastrados"
    
    def __str__(self):
        return '{}'.format(self.caixa)
