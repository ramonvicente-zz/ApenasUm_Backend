from django.shortcuts import render
from django.views.generic import View
from requests.auth import HTTPBasicAuth
import requests
import json
from apps.client.models import *

class TestAPIZoop(View):
    template_name = "dashboard.html"

    def get(self, request):
        # Criação do vendedor
        # data = { "taxpayer_id": "18032583491" }
        # url = 'https://api.zoop.ws/v1/marketplaces/3249465a7753536b62545a6a684b0000/sellers/individuals'
        # requisicao_vendedor = requests.post(url, data, headers={'Authorization': 'Basic enBrX3Rlc3RfRXpDa3pGRktpYkdRVTZIRnE3RVlWdXhJOg=='})
        # objeto_vendedor = json.loads(requisicao_vendedor.text)
        # print(objeto_vendedor['id'])

        id_vendedor = 'a32da232d0a347faa902eeda1a723071'

        # Criação do comprador
        data = { "first_name": "Joao", "last_name": "Silva"}
        url = 'https://api.zoop.ws/v1/marketplaces/3249465a7753536b62545a6a684b0000/buyers'
        requisicao_comprador = requests.post(url, data, headers={'Authorization': 'Basic enBrX3Rlc3RfRXpDa3pGRktpYkdRVTZIRnE3RVlWdXhJOg=='})
        print(requisicao_comprador.text)
        objeto_comprador = json.loads(requisicao_comprador.text)
        id_cliente = objeto_comprador['id']


        # Criação do cartão
        data = { "holder_name": "JOHN LENNON", "expiration_month": "01", "expiration_year": "19", "security_code": "000", "card_number": "4111111111111111"}
        url = 'https://api.zoop.ws/v1/marketplaces/3249465a7753536b62545a6a684b0000/cards/tokens'
        requisicao_novo_cartao = requests.post(url, data, headers={'Authorization': 'Basic enBrX3Rlc3RfRXpDa3pGRktpYkdRVTZIRnE3RVlWdXhJOg=='})
        print(requisicao_novo_cartao.text)
        objeto_novo_cartao = json.loads(requisicao_novo_cartao.text)
        token_cartao = objeto_novo_cartao['id']

        data = {"token": token_cartao, "customer": id_cliente}
        url = 'https://api.zoop.ws/v1/marketplaces/3249465a7753536b62545a6a684b0000/cards'
        requisicao_associacao_cartao = requests.post(url, data, headers={'Authorization': 'Basic enBrX3Rlc3RfRXpDa3pGRktpYkdRVTZIRnE3RVlWdXhJOg=='})
        print(requisicao_associacao_cartao.text)
        objeto_associacao_cartao = json.loads(requisicao_associacao_cartao.text)
        id_associacao_cartao = objeto_associacao_cartao['id']

        data = { "payment_type": "credit", "currency": "BRL", "description": "test 123", "customer": id_cliente, "on_behalf_of": id_vendedor, "amount": "10000", "capture": 'true'}
        url = 'https://api.zoop.ws/v1/marketplaces/3249465a7753536b62545a6a684b0000/transactions'
        requisicao_transacao = requests.post(url, data, headers={'Authorization': 'Basic enBrX3Rlc3RfRXpDa3pGRktpYkdRVTZIRnE3RVlWdXhJOg=='})
        print(requisicao_transacao.text)
        objeto_transacao = json.loads(requisicao_transacao.text)

        context = {'user': 'teste'}
        return render(request, self.template_name, context)

class Dashboard(View):
    template_name = "dashboard.html"        

    def get(self, request):

        context = {}
        return render(request, self.template_name, context)
