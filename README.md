# 🚀 MVP Gerenciador de Processos PDTIC (Streamlit + FastAPI)

## 📋 Sobre o Projeto

Este repositório contém o **MVP (Produto Mínimo Viável)** de um sistema de gerenciamento e monitoramento de processos, desenvolvido para auxiliar na **governança e execução do Plano Diretor de Tecnologia da Informação e Comunicação (PDTIC)**.

O objetivo é fornecer uma interface simples e funcional para o **cadastro, acompanhamento e conclusão das ações estratégicas do plano**, garantindo visibilidade e controle sobre os recursos de TI.

**Vídeo de apresentação do MVP + PDTIC:** https://youtu.be/kr_lzCCnGxQ

---

## ⚙️ Arquitetura

O sistema adota uma arquitetura modular, desacoplando a interface de usuário da lógica de dados:

| Componente | Tecnologia | Descrição |
|-------------|-------------|-----------|
| **Frontend** | [Streamlit](https://streamlit.io/) | Interface web simples e interativa para cadastro e visualização dos processos (`app_mvp_monitora.py`) |
| **Backend** | [FastAPI](https://fastapi.tiangolo.com/) | API leve e rápida para operações CRUD dos processos (`api.py`) |
| **Banco de Dados** | [SQLite3](https://www.sqlite.org/) | Armazenamento persistente e local dos dados (`processos.db`) |

---

## 🛠️ Tecnologias Utilizadas

| Camada | Tecnologia | Função |
|--------|-------------|--------|
| Frontend | Streamlit | Interface de usuário (UI) |
| Backend | FastAPI | Rotas e lógica de negócio |
| Banco de Dados | SQLite3 | Persistência local |
| Comunicação | `requests` (Python) | Conexão HTTP entre Streamlit e FastAPI |

---

## 🚀 Instalação e Execução

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/usuario/repositorio.git
cd nome-do-repositorio
```

### 2️⃣ Instalar Dependências
Instale as bibliotecas necessárias:
```bash
pip install streamlit fastapi "uvicorn[standard]" requests pydantic
```

### 3️⃣ Iniciar o Backend (API)
O backend deve ser iniciado primeiro, pois o Streamlit depende dele para acessar os dados.
```bash
uvicorn api:app --reload
```
### 4️⃣ Iniciar o Frontend (Streamlit)
Em outro terminal:
```bash
streamlit run app_mvp_monitora.py
```
O aplicativo será aberto automaticamente no seu navegador.

---

### 🔑 Funcionalidades da API

A API FastAPI gerencia a tabela processos do banco SQLite:

| Método | Endpoint | Descrição |
|-------------|-------------|-----------|
| POST | /processos/	| Cria um novo processo |
| GET	| /processos/	| Lista todos os processos |
| PUT	| /processos/{id}	| Atualiza o status ou dados de um processo |
| DELETE |	/processos/{id}	| Remove ou conclui um processo |

