````markdown
# SafeData - API de Gerenciamento de Dados Pessoais (LGPD)

Este projeto é uma aplicação Django com Django REST Framework (DRF), desenvolvida como parte de um trabalho acadêmico. A plataforma visa a **gestão segura de dados pessoais**, oferecendo recursos de controle de consentimento, exclusão de dados e autenticação via token — com foco na **conformidade com a LGPD** (Lei Geral de Proteção de Dados).

---

## ⚙️ Tecnologias Utilizadas

- Python 3.11+
- Django 5.2.1
- Django REST Framework
- MySQL
- Token Authentication (DRF)
- Middleware customizado (para controle de usuário atual)

---

## 📦 Instalação Local

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/safedata.git
cd safedata
````

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto com suas configurações de banco de dados MySQL:

```
DB_NAME=safedata
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=3306
```

### 5. Configure o banco de dados

Crie o banco de dados com o mesmo nome configurado no `.env` e execute as migrações:

```bash
python manage.py migrate
```

### 6. Crie um superusuário (opcional)

```bash
python manage.py createsuperuser
```

---

## 🚀 Executando a API

```bash
python manage.py runserver
```

Acesse: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔐 Autenticação

A API usa autenticação via token:

### Obter token

```http
POST /api/token/
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

Retorno:

```json
{
  "token": "seu_token_de_autenticacao"
}
```

Use esse token no header `Authorization` das requisições:

```
Authorization: Token seu_token_de_autenticacao
```

---

## 📌 Endpoints

| Verbo  | Rota                 | Descrição                                |
| ------ | -------------------- | ---------------------------------------- |
| GET    | /api/pessoas/        | Lista pessoas (autenticado)              |
| POST   | /api/pessoas/        | Cria uma nova pessoa                     |
| PUT    | /api/pessoas/{id}/   | Atualiza uma pessoa existente            |
| DELETE | /api/pessoas/{id}/   | Remove uma pessoa                        |
| GET    | /api/consentimentos/ | Lista consentimentos                     |
| POST   | /api/consentimentos/ | Cria um consentimento                    |
| POST   | /api/apagar-dados/   | Exclui dados pessoais com base no CPF    |
| POST   | /api/consentimento/  | Atualiza ou remove consentimento por CPF |
| POST   | /api/token/          | Gera token de autenticação               |

---

## 🧩 Estrutura do Projeto

```
├── app/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── signals.py
│   ├── middleware.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
├── manage.py
└── .env
```

---

## 📋 Considerações Finais

* Este projeto é voltado a fins **educacionais**, mas implementa práticas reais de conformidade com a LGPD.
* Pode ser expandido para incluir recursos como auditoria, criptografia de dados sensíveis e exportação de dados.

---
