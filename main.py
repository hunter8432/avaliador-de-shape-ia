import streamlit as st
import pandas as pd
from PIL import Image

# Configuração da página
st.set_page_config(page_title="Avaliador de Shape", page_icon="💪", layout="centered")
st.title("💪 Avaliador de Shape com Inteligência Artificial")

st.markdown("""
Bem-vindo ao protótipo do avaliador de shape. 
Como profissional de DevOps, este app será o nosso laboratório de testes!
""")

# --- CAMPO DE UPLOAD DA FOTO ---
st.subheader("📸 Envie a foto do seu Shape")
foto_enviada = st.file_uploader("Escolha uma imagem (JPG, PNG)", type=["jpg", "jpeg", "png"])

if foto_enviada is not None:
    # Abre e exibe a imagem na tela
    imagem = Image.open(foto_enviada)
    st.image(imagem, caption="Foto carregada com sucesso!", use_container_width=True)
    
    # Botão para simular a análise da IA
    if st.button("🚀 Analisar Shape com IA"):
        with st.spinner("A IA está analisando sua simetria e proporções..."):
            # Aqui no futuro entrará a chamada da API da IA (OpenAI/Gemini)
            # Por enquanto, colocamos uma resposta estática (Mock) para testar o fluxo
            st.success("Análise concluída!")
            st.subheader("📝 Relatório da IA (Simulação)")
            st.write("- **Proporção Ombro/Cintura:** Excelente estética em V.")
            st.write("- **Estimativa de BF (Gordura):** Cerca de 12-14%.")
            st.write("- **Ponto Forte:** Deltoides (ombros) bem desenvolvidos.")
            st.write("- **Foco de Treino:** Sugerido maior volume em membros inferiores.")
else:
    st.info("Aguardando o envio de uma foto para iniciar a análise.")
