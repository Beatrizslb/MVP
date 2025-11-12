import streamlit as st
import requests
from datetime import date

st.title("⚙️ Gerenciador de Processos")
st.sidebar.header("Cadastrar Novo Processo")

id = st.sidebar.number_input("ID", step=1)
nome = st.sidebar.text_input("Nome do Processo")
tipo = st.sidebar.selectbox("Tipo", ["Planejamento", "Desenvolvimento", "Treinamento de IA", "Teste", "Implantação"])
setor = st.sidebar.selectbox("Setor Responsável", ["Front-end", "Back-end", "Banco de Dados", "IA", "Design", "Outro"])
status = st.sidebar.selectbox("Status", ["Pendente", "Em andamento", "Concluído"])
data_inicio = st.sidebar.date_input("Data de Início", date.today())
data_fim = st.sidebar.date_input("Previsão de Término", date.today())

if st.sidebar.button("Salvar Processo"):
    data = {
        "id": id,
        "nome": nome,
        "tipo": tipo,
        "setor": setor,
        "status": status,
        "data_inicio": str(data_inicio),
        "data_fim": str(data_fim),
    }
    requests.post("http://127.0.0.1:8001/processos/", json=data)
    st.sidebar.success("Processo registrado com sucesso!")

st.subheader("📋 Lista de Processos")
dados = requests.get("http://127.0.0.1:8001/processos/").json()

for p in dados["processos"]:
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(f"### {p['nome']}")
        st.write(f"🧩 Tipo: {p['tipo']}")
        st.write(f"👥 Setor: {p['setor']}")
        st.write(f"📅 Início: {p['data_inicio']} → Fim previsto: {p['data_fim']}")
        st.write(f"📊 Status atual: **{p['status']}**")

    with col2:
        if st.button(f"Concluir {p['id']}", key=f"btn_concluir_{p['id']}"):
            requests.delete(f"http://127.0.0.1:8001/processos/{p['id']}")
            st.success(f"Processo {p['nome']} concluído e removido.")
            st.rerun()


            if st.button(f"Salvar {p['id']}", key=f"save_{p['id']}"):
                requests.put(f"http://127.0.0.1:8001/processos/{p['id']}", params={"novo_status": novo_status})
                st.success(f"Status do processo {p['nome']} atualizado.")
                st.rerun()

    st.divider()
