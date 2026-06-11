import requests

ENDPOINT = "https://compassuol.serverest.dev"

#response = requests.get(ENDPOINT)
#print(response.status_code)

def test_call_endpoint ():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    pass

# funções para cada endpoint de usuários

def listar_usuarios():
    response = requests.get(ENDPOINT + "/usuarios")
    return response

def cadastrar_usuario(dados):
    response = requests.post(ENDPOINT + "/usuarios", json=dados)
    return response

def buscar_usuario(id):
    response = requests.get(ENDPOINT + "/usuarios/" + id)
    return response

def atualizar_usuario(id, dados):
    response = requests.put(ENDPOINT + "/usuarios/" + id, json=dados)
    return response

def excluir_usuario(id):
    response = requests.delete(ENDPOINT + "/usuarios/" + id)
    return response