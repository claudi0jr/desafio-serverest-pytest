import requests

BASE_URL = "https://compassuol.serverest.dev"

# funções para cada endpoint de usuários

def listar_usuarios():
    response = requests.get(BASE_URL + "/usuarios")
    return response

def cadastrar_usuario(dados):
    response = requests.post(BASE_URL + "/usuarios", json=dados)
    return response

def buscar_usuario(id):
    response = requests.get(BASE_URL + "/usuarios/" + id)
    return response

def atualizar_usuario(id, dados):
    response = requests.put(BASE_URL + "/usuarios/" + id, json=dados)
    return response

def excluir_usuario(id):
    response = requests.delete(BASE_URL + "/usuarios/" + id)
    return response