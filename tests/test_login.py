import requests

ENDPOINT = "https://compassuol.serverest.dev"


# testa login com credenciais corretas
def test_login_credenciais_corretas(usuario_cadastrado):
    dados = {
        "email": usuario_cadastrado["email"],
        "password": "teste123"
    }
    response = requests.post(ENDPOINT + "/login", json=dados)
    body = response.json()

    assert response.status_code == 200
    assert "message" in body
    assert "authorization" in body
    assert isinstance(body["message"], str)
    assert isinstance(body["authorization"], str)


# testa login com senha errada
def test_login_senha_errada(usuario_cadastrado):
    dados = {
        "email": usuario_cadastrado["email"],
        "password": "senhaerrada"
    }
    response = requests.post(ENDPOINT + "/login", json=dados)
    body = response.json()

    assert response.status_code == 401
    assert "message" in body
    assert isinstance(body["message"], str)


# testa login com email inexistente
def test_login_email_inexistente():
    dados = {
        "email": "emailquenaoexiste@teste.com",
        "password": "teste123"
    }
    response = requests.post(ENDPOINT + "/login", json=dados)
    body = response.json()

    assert response.status_code == 401
    assert "message" in body
    assert isinstance(body["message"], str)


# testa login com campos vazios
def test_login_campos_vazios():
    dados = {
        "email": "",
        "password": ""
    }
    response = requests.post(ENDPOINT + "/login", json=dados)
    body = response.json()

    assert response.status_code == 400
    assert "message" in body or "email" in body or "password" in body
