import pytest
import uuid
import requests

ENDPOINT = "https://compassuol.serverest.dev"

# geracao de email unico para cada teste, evita email ja cadastrado
def gerar_email_unico():
    return "usuario_" + str(uuid.uuid4()) + "@teste.com"

# fixture para criar um usuario antes do teste e deletar depois do teste
@pytest.fixture
def usuario_cadastrado():
    email = gerar_email_unico()
    dados = {
        "nome": "Claudio Fixture",
        "email": email,
        "password": "teste123",
        "administrador": "false"
    }

    response = requests.post(ENDPOINT + "/usuarios", json=dados)
    usuario = response.json()

    # adiciona o email gerado ao usuario para usar nos testes de email duplicado
    usuario["email"] = email

    yield usuario

    # deleta o usuario criado apos o teste
    requests.delete(ENDPOINT + "/usuarios/" + usuario["_id"])