# Plano de Testes — ServeRest API

## Objetivo

Validar o comportamento dos endpoints de Usuários, Login e Produtos da API ServeRest, garantindo que as respostas estejam corretas tanto em status code quanto na estrutura completa do JSON retornado.

---

## Estratégia

- **Tipo de teste:** Testes funcionais de API (caixa-preta)
- **Camada:** Integração — chamadas HTTP diretas à API
- **Ferramentas:** Python 3.13, Pytest, Requests

---

## Escopo

### O que está coberto

- Endpoint `/usuarios` — CRUD completo e validações de campos obrigatórios
- Endpoint `/login` — autenticação com cenários válidos e inválidos
- Endpoint `/produtos` — CRUD completo com e sem autenticação de administrador

### O que ficou fora

- Endpoint `/carrinhos` — fora do escopo deste desafio

---

## Cenários a implementar

### Usuários (`/usuarios`) — já implementado na Semana 3

| # | Cenário | Método | Status esperado |
|---|---------|--------|-----------------|
| 1 | Listar usuários | GET | 200 |
| 2 | Listar retorna chave "usuarios" no JSON | GET | 200 |
| 3 | Cadastrar usuário com dados válidos | POST | 201 |
| 4 | Cadastrar retorna mensagem de sucesso | POST | 201 |
| 5 | Cadastrar com email duplicado | POST | 400 |
| 6 | Cadastrar sem o campo nome | POST | 400 |
| 7 | Cadastrar sem o campo email | POST | 400 |
| 8 | Cadastrar sem o campo password | POST | 400 |
| 9 | Buscar usuário por ID válido | GET | 200 |
| 10 | Buscar usuário com ID inexistente | GET | 400 |
| 11 | Atualizar usuário existente | PUT | 200 |
| 12 | Excluir usuário existente | DELETE | 200 |

---

### Login (`/login`)

| # | Cenário | Método | Status esperado |
|---|---------|--------|-----------------|
| 1 | Login com credenciais corretas | POST | 200 |
| 2 | Login com senha errada | POST | 401 |
| 3 | Login com email inexistente | POST | 401 |
| 4 | Login com campos vazios | POST | 400 |

---

### Produtos (`/produtos`)

| # | Cenário | Método | Status esperado |
|---|---------|--------|-----------------|
| 1 | Listar produtos | GET | 200 |
| 2 | Cadastrar produto com token de admin | POST | 201 |
| 3 | Cadastrar produto sem token | POST | 401 |
| 4 | Buscar produto por ID válido | GET | 200 |
| 5 | Atualizar produto com token de admin | PUT | 200 |
| 6 | Excluir produto com token de admin | DELETE | 200 |

---

## Critérios de qualidade

Um teste é considerado pronto quando:

1. Valida o **status code** da resposta
2. Valida a **estrutura completa do JSON** retornado (chaves presentes e tipos esperados)


