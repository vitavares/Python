import streamlit as st
import pandas as pd

@st.cache_data
def carregar_dados():
    tabela = pd.read_csv('data/resultados.csv')
    return(tabela)

st.set_page_config(page_title="Vitória Tavares")

with st.container():
    st.title("Dashboard de contratos")
    st.write("Informações sobre os contratos fechados de uma empresa no mês de maio.")


with st.container():
    st.write("---")
    qtd_dias = st.selectbox("Periodo", ["5D", "10D", "15D", "20D", "25", "30"])
    num_dias = int(qtd_dias.replace("D", ""))
    dados = carregar_dados()
    dados = dados[-num_dias:]
    st.area_chart(data = dados, x='Data', y='Contratos')