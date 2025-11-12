from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI(title="API Gerenciador de Processos - PMLI")

# Modelo de dados do processo
class Processo(BaseModel):
    id: int
    nome: str
    tipo: str
    setor: str
    status: str
    data_inicio: str
    data_fim: str

# Função de conexão com o banco
def db_connection():
    conn = sqlite3.connect("processos.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS processos (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            tipo TEXT,
            setor TEXT,
            status TEXT,
            data_inicio TEXT,
            data_fim TEXT
        )
    """)
    return conn

# Rota para criar um processo
@app.post("/processos/")
def criar_processo(processo: Processo):
    try:
        conn = db_connection()
        conn.execute(
            "INSERT INTO processos VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                processo.id,
                processo.nome,
                processo.tipo,
                processo.setor,
                processo.status,
                processo.data_inicio,
                processo.data_fim
            )
        )
        conn.commit()
        return {"mensagem": "Processo criado com sucesso!"}
    except Exception as e:
        print("ERRO AO CRIAR PROCESSO:", e)
        return {"erro": str(e)}

# Rota para listar processos
@app.get("/processos/")
def listar_processos():
    try:
        conn = db_connection()
        cursor = conn.cursor()
        processos = cursor.execute("SELECT * FROM processos").fetchall()
        lista = [
            {
                "id": p[0],
                "nome": p[1],
                "tipo": p[2],
                "setor": p[3],
                "status": p[4],
                "data_inicio": p[5],
                "data_fim": p[6],
            }
            for p in processos
        ]
        return {"processos": lista}
    except Exception as e:
        print("ERRO AO LISTAR PROCESSOS:", e)
        return {"erro": str(e)}

# Rota para atualizar status de um processo (ex: marcar como concluído)
@app.put("/processos/{id}")
def atualizar_status(id: int, novo_status: str):
    try:
        conn = db_connection()
        conn.execute("UPDATE processos SET status = ? WHERE id = ?", (novo_status, id))
        conn.commit()
        return {"mensagem": f"Status do processo {id} atualizado para '{novo_status}'."}
    except Exception as e:
        print("ERRO AO ATUALIZAR PROCESSO:", e)
        return {"erro": str(e)}

# Rota para excluir um processo
@app.delete("/processos/{id}")
def deletar_processo(id: int):
    try:
        conn = db_connection()
        conn.execute("DELETE FROM processos WHERE id = ?", (id,))
        conn.commit()
        return {"mensagem": f"Processo {id} removido com sucesso!"}
    except Exception as e:
        print("ERRO AO DELETAR PROCESSO:", e)
        return {"erro": str(e)}
