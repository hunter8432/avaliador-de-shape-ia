import streamlit as st
import pandas as pd

# Inicializa a sessão para salvar os dados mesmo quando a página recarregar
if 'historico_treino' not in st.session_state:
    st.session_state.historico_treino = []

st.set_page_config(page_title="Evolução de Treino", page_icon="💪", layout="centered")
st.title("💪 Acompanhamento de Treino e Evolução")

# --- FORMULÁRIO DE ENTRADA NA PÁGINA ---
st.subheader("📝 Cadastrar Novo Registro")
with st.form(key='formulario_treino', clear_on_submit=True):
    col1, col2 = st.columns(2)
    
    with col1:
        mes = st.selectbox("Mês", ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"])
        exercicio = st.text_input("Exercício Principal")
        corpo = st.text_input("Parte do Corpo Medida (ex: Bíceps)")
        
    with col2:
        peso = st.number_input("Peso Corporal (kg)", min_value=0.0, step=0.1, format="%.1f")
        carga = st.number_input("Carga do Exercício (kg)", min_value=0.0, step=0.5, format="%.1f")
        medida = st.number_input("Medida Corporal (cm)", min_value=0.0, step=0.1, format="%.1f")
        
    botao_enviar = st.form_submit_with_button("Adicionar Dados")

# --- LÓGICA DE SALVAMENTO ---
if botao_enviar:
    if exercicio and corpo:  # Garante que os campos de texto não estão vazios
        novo_registro = {
            'Mês': mes,
            'Exercicio': exercicio,
            'Peso corporal': peso,
            'Carga dos Exercicios': carga,
            'Medida corporais': medida,
            'Corpo': corpo
        }
        st.session_state.historico_treino.append(novo_registro)
        st.success("Dados adicionados com sucesso!")
    else:
        st.error("Por favor, preencha todos os campos de texto.")

# --- EXIBIÇÃO DA TABELA NA PÁGINA ---
st.subheader("📊 Seus Dados Cadastrados")
if st.session_state.historico_treino:
    df_treino = pd.DataFrame(st.session_state.historico_treino)
    
    # Exibe a tabela interativa do Pandas na página web
    st.dataframe(df_treino, use_container_width=True)
    
    # Botão opcional para baixar os dados em formato CSV
    csv = df_treino.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Baixar Tabela (CSV)", csv, "dados_treino.csv", "text/csv")
else:
    st.info("Nenhum dado cadastrado ainda. Use o formulário acima para começar!")
