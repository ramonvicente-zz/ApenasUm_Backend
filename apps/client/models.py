from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from apps.common.fields import JSONField
from apps.common.models import BestPraticesModel
from apps.core.models import Address, State, City
from django.db.models.signals import post_save

import re

class CartaoVigente(BestPraticesModel):
    MODO_CARTAO = (
        ('Físico', 'Físico'),
        ('Virtual', 'Virtual'),
    )
    numero = models.IntegerField(blank=True, null=True)
    cvc = models.IntegerField(blank=True, null=True)
    nome_cartao = models.CharField(blank=True, null=True, max_length=200)
    validade = models.CharField(blank=True, null=True, max_length=200)
    bandeira = models.CharField(blank=True, null=True, max_length=200)
    is_vigente = models.BooleanField(default=False)
    data_validade = models.DateField(blank=True, null=True)
    quantidade_uso = models.IntegerField(blank=True, null=True)
    modo_cartao = models.CharField(blank=True, null=True, max_length=10, choices=MODO_CARTAO)

    class Meta:
        verbose_name = "Cartão Vigente"
    
    def __str__(self):
        return '{}'.format(self.nome_cartao)


class CartaoReal(BestPraticesModel):
    TIPO_CARTAO = (
        ('Débito', 'Débito'),
        ('Crédito', 'Crédito'),
    )
    id_zoop = models.CharField(blank=True, null=True, max_length=200)
    numero = models.IntegerField(blank=True, null=True)
    cvc = models.IntegerField(blank=True, null=True)
    nome_cartao = models.CharField(blank=True, null=True, max_length=200)
    validade = models.CharField(blank=True, null=True, max_length=200)
    bandeira = models.CharField(blank=True, null=True, max_length=200)
    is_prioritario = models.BooleanField(default=False)
    data_validade = models.DateField(blank=True, null=True)
    quantidade_uso = models.IntegerField(blank=True, null=True)
    tipo_cartao = models.CharField(blank=True, null=True, max_length=10, choices=TIPO_CARTAO)

    class Meta:
        verbose_name = "Cartão Real"
    
    def __str__(self):
        return '{}'.format(self.nome_cartao)


class Usuario(BestPraticesModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    # BASIC INFO
    id_zoop = models.CharField(blank=True, null=True, max_length=200)
    nome_completo = models.CharField('Nome Completo', max_length=200)
    email = models.EmailField('Email', max_length=100)
    cpf = models.CharField('CPF', max_length=14, blank=True, null=True)
    telefone = models.CharField('Telefone', max_length=20, blank=True, null=True)
    cartao_vigencia = models.ManyToManyField(CartaoVigente, blank=True)
    cartao_real = models.ManyToManyField(CartaoReal, blank=True)
    # CONFIRMATION INFO
    sms_code = models.CharField(max_length=4, blank=True, null=True)
    sms_date = models.DateTimeField(blank=True, null=True)
    sms_resends = models.IntegerField(default=0, blank=True, null=True)
    confirmation_sms = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Usuário"
    
    def __str__(self):
        return '{}'.format(self.nome_completo)


class Transacao(BestPraticesModel):
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, blank=True, null=True)
    cartao_vigencia = models.ForeignKey(CartaoVigente, on_delete=models.DO_NOTHING, blank=True, null=True)
    cartao_real = models.ForeignKey(CartaoReal, on_delete=models.DO_NOTHING, blank=True, null=True)
    data_transacao = models.DateField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=14, decimal_places=12, blank=True, null=True)
    longitude = models.DecimalField(max_digits=14, decimal_places=12, blank=True, null=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    local = models.CharField(blank=True, null=True, max_length=200)
    cnpj_logista = models.CharField(blank=True, null=True, max_length=200)
    is_parcelado = models.BooleanField(default=False)
    quantidade_parcelas = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Transação"
    
    def __str__(self):
        return '{}'.format(self.usuario)

