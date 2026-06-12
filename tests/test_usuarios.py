import uuid
import requests

ENDPOINT = "https://compassuol.serverest.dev"

# gera um email unico para cada execucao dos testes
def gerar_email_unico():
    return "usuario_" + str(uuid.uuid4()) + "@teste.com"


# testa se a listagem de usuarios retorna status 200
def test_listar_usuarios_retorna_200():
    response = requests.get(ENDPOINT + "/usuarios")
    assert response.status_code == 200


# testa se a listagem retorna a chave "usuarios" no json
def test_listar_usuarios_retorna_lista():
    response = requests.get(ENDPOINT + "/usuarios")
    assert "usuarios" in response.json()


# testa cadastro de usuario com dados validos
def test_cadastrar_usuario_valido():
    dados = {
        "nome": "Claudio Teste",
        "email": gerar_email_unico(),
        "password": "teste123",
        "administrador": "false"
    }
    response = requests.post(ENDPOINT + "/usuarios", json=dados)
    assert response.status_code == 201


# testa se ao cadastrar um usuario, a mensagem de sucesso aparece
def test_cadastrar_usuario_retorna_mensagem_sucesso():
    dados = {
        "nome": "Claudio Teste",
        "email": gerar_email_unico(),
        "password": "teste123",
        "administrador": "false"
    }
    response = requests.post(ENDPOINT + "/usuarios", json=dados)
    assert response.json()["message"] == "Cadastro realizado com sucesso"


# testa cadastro com email ja existente
def test_cadastrar_usuario_email_duplicado_retorna_400(usuario_cadastrado):
    dados = {
        "nome": "Outro Usuario",
        "email": usuario_cadastrado["email"],
        "password": "teste123",
        "administrador": "false"
    }
    response = requests.post(ENDPOINT + "/usuarios", json=dados)
    assert response.status_code == 400


# testa cadastro sem o campo nome
def test_cadastrar_usuario_sem_nome_retorna_400():
    dados = {
        "email": gerar_email_unico(),
        "password": "teste123",
        "administrador": "false"
    }
    response = requests.post(ENDPOINT + "/usuarios", json=dados)
    assert response.status_code == 400


# testa cadastro sem o campo email
def test_cadastrar_usuario_sem_email_retorna_400():
    dados = {
        "nome": "Claudio Teste",
        "password": "teste123",
        "administrador": "false"
    }
    response = requests.post(ENDPOINT + "/usuarios", json=dados)
    assert response.status_code == 400


# testa cadastro sem o campo password
def test_cadastrar_usuario_sem_password_retorna_400():
    dados = {
        "nome": "Claudio Teste",
        "email": gerar_email_unico(),
        "administrador": "false"
    }
    response = requests.post(ENDPOINT + "/usuarios", json=dados)
    assert response.status_code == 400


# testa busca de usuario por id valido
def test_buscar_usuario_por_id(usuario_cadastrado):
    id = usuario_cadastrado["_id"]
    response = requests.get(ENDPOINT + "/usuarios/" + id)
    assert response.status_code == 200


# testa busca de usuario com id inexistente
def test_buscar_usuario_id_inexistente_retorna_400():
    response = requests.get(ENDPOINT + "/usuarios/idquenaoexiste123")
    assert response.status_code == 400


# testa atualizacao de usuario existente
def test_atualizar_usuario(usuario_cadastrado):
    id = usuario_cadastrado["_id"]
    dados_atualizados = {
        "nome": "Claudio Atualizado",
        "email": gerar_email_unico(),
        "password": "teste123",
        "administrador": "false"
    }
    response = requests.put(ENDPOINT + "/usuarios/" + id, json=dados_atualizados)
    assert response.status_code == 200


# testa exclusao de usuario existente
def test_excluir_usuario(usuario_cadastrado):
    id = usuario_cadastrado["_id"]
    response = requests.delete(ENDPOINT + "/usuarios/" + id)
    assert response.status_code == 200