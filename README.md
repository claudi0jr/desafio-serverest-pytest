# Desafio Semana 3 - Testes Automatizados ServeRest

Projeto criado como parte do desafio da semana 3 do curso, com o objetivo de praticar testes automatizados de API usando Python e Pytest.

A API testada é a [ServeRest](https://compassuol.serverest.dev/), que simula uma loja virtual.

## O que foi testado

### Usuários
- Listar usuários
- Cadastrar usuário válido
- Cadastrar usuário com email duplicado
- Cadastrar usuário sem nome
- Cadastrar usuário sem email
- Cadastrar usuário sem password
- Buscar usuário por ID
- Buscar usuário com ID inexistente
- Atualizar usuário
- Excluir usuário

### Login
- Login com credenciais corretas
- Login com senha errada
- Login com email inexistente
- Login com campos vazios

### Produtos
- Listar produtos
- Cadastrar produto com token de administrador
- Cadastrar produto sem token
- Buscar produto por ID
- Atualizar produto
- Excluir produto

## Tecnologias utilizadas

- Python 3.13
- Pytest
- Requests

## Como rodar o projeto

**1. Clone o repositório**
```bash
git clone https://github.com/claudi0jr/desafio-serverest-pytest.git
cd desafio-serverest-pytest
```

**2. Crie e ative o ambiente virtual**

Mac/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Rode os testes**
```bash
pytest -v
```

## Estrutura do projeto

```
desafio-serverest-pytest/
├── tests/
│   ├── conftest.py         # fixtures de usuário, admin e produto
│   ├── test_usuarios.py    # testes do endpoint de usuários
│   ├── test_login.py       # testes do endpoint de login
│   └── test_produtos.py    # testes do endpoint de produtos
├── pytest.ini              # configuração do pytest
├── requirements.txt        # dependências do projeto
├── PLANO-DE-TESTES.md      # planejamento da suíte de testes
└── README.md
```

## Análise de cobertura

### Método utilizado

A cobertura foi calculada com base no método de **cobertura por operações**, conforme descrito no artigo [Como verificar a cobertura de testes da API REST](https://medium.com/revista-dtar/como-verificar-a-cobertura-de-testes-da-api-rest-9e2f745564b).

O método consiste em mapear todas as operações disponíveis na API (combinação de método HTTP + endpoint) e verificar quantas estão cobertas por pelo menos um teste.

### Cobertura atingida

| Operação | Coberta |
|----------|---------|
| POST /login | ✅ |
| GET /usuarios | ✅ |
| POST /usuarios | ✅ |
| GET /usuarios/{_id} | ✅ |
| PUT /usuarios/{_id} | ✅ |
| DELETE /usuarios/{_id} | ✅ |
| GET /produtos | ✅ |
| POST /produtos | ✅ |
| GET /produtos/{_id} | ✅ |
| PUT /produtos/{_id} | ✅ |
| DELETE /produtos/{_id} | ✅ |
| GET /carrinhos | ❌ |
| POST /carrinhos | ❌ |
| GET /carrinhos/{_id} | ❌ |
| DELETE /carrinhos/concluir-compra | ❌ |
| DELETE /carrinhos/cancelar-compra | ❌ |

**Cobertura total da API: 11/16 = 68,75%**

### O que ficou fora e por quê

O endpoint `/carrinhos` foi excluído do escopo deste teste por decisão prévia documentada no `PLANO-DE-TESTES.md`. O foco foi cobrir completamente os endpoints de Usuários, Login e Produtos, conforme solicitado.