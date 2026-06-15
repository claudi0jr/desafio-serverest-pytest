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
        "administrador": "false",
    }

    response = requests.post(ENDPOINT + "/usuarios", json=dados)
    usuario = response.json()

    # adiciona o email gerado ao usuario para usar nos testes de email duplicado
    usuario["email"] = email

    yield usuario

    # deleta o usuario criado apos o teste
    requests.delete(ENDPOINT + "/usuarios/" + usuario["_id"])


# fixture admin, faz login e retorna o token
@pytest.fixture
def admin_token():
    email = gerar_email_unico()
    dados = {
        "nome": "Admin Fixture",
        "email": email,
        "password": "teste123",
        "administrador": "true",
    }

    response = requests.post(ENDPOINT + "/usuarios", json=dados)
    admin = response.json()

    login_response = requests.post(
        ENDPOINT + "/login", json={"email": email, "password": "teste123"}
    )
    token = login_response.json()["authorization"]

    yield token

    # deleta o usuario administrador criado apos o teste
    requests.delete(ENDPOINT + "/usuarios/" + admin["_id"])


# fixture que cria um produto antes do teste e deleta depois
@pytest.fixture
def produto_cadastrado(admin_token):
    dados = {
        "nome": "Produto Fixture " + str(uuid.uuid4()),
        "preco": 100,
        "descricao": "Produto criado pela fixture",
        "quantidade": 10,
    }

    response = requests.post(
        ENDPOINT + "/produtos", json=dados, headers={"Authorization": admin_token}
    )
    produto = response.json()

    yield produto

    # deleta o produto criado apos o teste
    requests.delete(
        ENDPOINT + "/produtos/" + produto["_id"], headers={"Authorization": admin_token}
    )
