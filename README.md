# Desafio Semana 3 - Testes Automatizados ServeRest

Projeto criado como parte do desafio da semana 3 do curso, com o objetivo de praticar testes automatizados de API usando Python e Pytest.

A API testada é a [ServeRest](https://compassuol.serverest.dev/), que simula uma loja virtual.

## O que foi testado

Todos os testes cobrem o endpoint de **Usuários** da ServeRest:

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
│   ├── conftest.py       # fixture que cria e deleta usuário para os testes
│   └── test_usuarios.py  # testes do endpoint de usuários
├── pytest.ini            # configuração do pytest
├── requirements.txt      # dependências do projeto
└── README.md
```