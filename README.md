# 🐾 Pet Resgate API

API desenvolvida com **FastAPI** para o projeto **Pet Resgate**, um sistema de gerenciamento de animais resgatados, adotantes e responsáveis. Esta API fornece endpoints RESTful para realizar operações de cadastro, consulta, atualização e remoção de dados relacionados a usuários, pets e adoções.

---

## 🚀 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/) – Framework moderno e rápido para APIs
- [SQLAlchemy](https://www.sqlalchemy.org/) – ORM para manipulação do banco de dados
- [PostgreSQL](https://www.postgresql.org/) – Banco de dados relacional
- [Pydantic](https://pydantic-docs.helpmanual.io/) – Validação e tipagem dos dados
- [Uvicorn](https://www.uvicorn.org/) – Servidor ASGI para execução da aplicação

---

## 📁 Estrutura de Pastas

```
PetResgate/
│
├── models/             # Modelos ORM com SQLAlchemy
│   ├── usuario.py
│   ├── pet.py
│   └── ...
│
├── schemas/            # Esquemas Pydantic
│   ├── usuario.py
│   ├── pet.py
│   └── ...
│
├── routers/            # Rotas da API organizadas por módulo
│   ├── usuario.py
│   ├── pet.py
│   └── ...
│
├── database/           # Configuração da conexão com o banco
│   └── connection.py
│
├── main.py             # Ponto de entrada da aplicação
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação
```

---

## ⚙️ Como Rodar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/pet-resgate-api.git
cd pet-resgate-api
```

### 2. Crie e ative um ambiente virtual (opcional)

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate    # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

No arquivo `database/connection.py`, atualize a URL de conexão com o PostgreSQL:

```python
DATABASE_URL = "postgresql://usuario:senha@localhost:5432/petresgate"
```

Crie o banco com esse nome no seu PostgreSQL e rode as migrações (se estiver usando).

### 5. Rode a aplicação

```bash
uvicorn main:app --reload
```

Acesse a documentação interativa:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🛠 Funcionalidades

- 🔐 Cadastro e login de usuários
- 🐶 Cadastro de pets
- 📄 Listagem, edição e exclusão de pets
- 🏠 Adoção de pets
- 📬 Sistema de notificação (em desenvolvimento)

---

## 🐞 Possíveis Erros e Soluções

**Erro**: `sqlalchemy.exc.NoForeignKeysError: Can't find any foreign key relationships...`  
**Solução**: Verifique se você definiu corretamente os relacionamentos e as chaves estrangeiras nos seus modelos.

---

## ✨ Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License**.

---

## 👩‍💻 Desenvolvido por

[Jasmin Shadday](https://github.com/jasmin-dev),
[Vithor Nelson](https://github.com/VithorNelson) e
[Nicolly Sampaio](https://github.com/nicsampaio)
