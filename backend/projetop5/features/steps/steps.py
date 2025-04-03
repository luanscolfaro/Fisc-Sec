from behave import given, when, then
from django.test import Client
import json  # Para converter os dados para JSON

@given("que tenho os dados de uma reclamação válida")
def step_given_dados_reclamacao_valida(context):
    context.dados_reclamacao = {
        "nome": "João Silva",
        "email": "joao@example.com",
        "telefone": "11987654321",
        "descricao": "Há um buraco grande na rua principal."
    }

@when("eu envio uma solicitação POST para criar a reclamação")
def step_when_enviar_reclamacao(context):
    context.client = Client()
    context.response = context.client.post(
        "/api/reclamacoes/",
        data=json.dumps(context.dados_reclamacao),  # Convertendo os dados para JSON
        content_type="application/json"
    )

@then("o sistema deve retornar um status 201")
def step_then_verificar_status(context):
    assert context.response.status_code == 201, (
        f"Esperado 201, mas recebeu {context.response.status_code}. "
        f"Resposta: {context.response.content.decode()}"
    )
