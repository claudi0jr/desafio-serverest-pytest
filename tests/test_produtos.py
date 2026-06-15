import uuid
import requests

ENDPOINT = "https://compassuol.serverest.dev"


# testa se a listagem de produtos retorna status 200 e estrutura correta
def test_listar_produtos():
    response = requests.get(ENDPOINT + "/produtos")
    body = response.json()

    assert response.status_code == 200
    assert "produtos" in body
    assert isinstance(body["produtos"], list)
    assert "quantidade" in body


# testa cadastro de produto com token de administrador
def test_cadastrar_produto_com_token(admin_token):
    dados = {
        "nome": "Produto Teste " + str(uuid.uuid4()),
        "preco": 50,
        "descricao": "Descricao do produto",
        "quantidade": 5,
    }
    response = requests.post(
        ENDPOINT + "/produtos", json=dados, headers={"Authorization": admin_token}
    )
    body = response.json()

    assert response.status_code == 201
    assert "message" in body
    assert "_id" in body
    assert isinstance(body["message"], str)
    assert isinstance(body["_id"], str)


# testa cadastro de produto sem token retorna 401
def test_cadastrar_produto_sem_token():
    dados = {
        "nome": "Produto Sem Token " + str(uuid.uuid4()),
        "preco": 50,
        "descricao": "Descricao do produto",
        "quantidade": 5,
    }
    response = requests.post(ENDPOINT + "/produtos", json=dados)
    body = response.json()

    assert response.status_code == 401
    assert "message" in body
    assert isinstance(body["message"], str)


# testa busca de produto por ID valido
def test_buscar_produto_por_id(produto_cadastrado):
    id = produto_cadastrado["_id"]
    response = requests.get(ENDPOINT + "/produtos/" + id)
    body = response.json()

    assert response.status_code == 200
    assert "_id" in body
    assert "nome" in body
    assert "preco" in body
    assert "descricao" in body
    assert "quantidade" in body


# testa atualizacao de produto com token de administrador
def test_atualizar_produto(produto_cadastrado, admin_token):
    id = produto_cadastrado["_id"]
    dados_atualizados = {
        "nome": "Produto Atualizado " + str(uuid.uuid4()),
        "preco": 200,
        "descricao": "Descricao atualizada",
        "quantidade": 20,
    }
    response = requests.put(
        ENDPOINT + "/produtos/" + id,
        json=dados_atualizados,
        headers={"Authorization": admin_token},
    )
    body = response.json()

    assert response.status_code == 200
    assert "message" in body
    assert isinstance(body["message"], str)


# testa exclusao de produto com token de administrador
def test_excluir_produto(produto_cadastrado, admin_token):
    id = produto_cadastrado["_id"]
    response = requests.delete(
        ENDPOINT + "/produtos/" + id, headers={"Authorization": admin_token}
    )
    body = response.json()

    assert response.status_code == 200
    assert "message" in body
    assert isinstance(body["message"], str)
