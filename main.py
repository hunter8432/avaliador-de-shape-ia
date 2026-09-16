import streamlit as st
from PIL import Image
from google import genai
import os
from dotenv import load_dotenv
import io  # <-- Adicionado para manipular os bytes na memória

load_dotenv()

st.set_page_config(
    page_title="Avaliador de Shape",
    page_icon="💪",
    layout="centered"
)

st.title("💪 Avaliador de Shape com Inteligência Artificial")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    api_key = st.text_input(
        "Insira sua Gemini API Key:",
        type="password"
    ).strip()

if api_key:
    client = genai.Client(api_key=api_key)
else:
    st.warning("⚠️ Configure sua GEMINI_API_KEY.")

st.subheader("📸 Envie a foto do seu Shape")

foto_enviada = st.file_uploader(
    "Escolha uma imagem",
    type=["jpg", "jpeg", "png"]
)

if foto_enviada is not None:
    # Abre a imagem original
    imagem_original = Image.open(foto_enviada)

    st.image(
        imagem_original,
        caption="Foto carregada com sucesso!",
        use_container_width=True
    )

    if st.button("🚀 Analisar Shape com IA Real"):
        if not api_key:
            st.error("Por favor, insira uma API Key.")
        else:
            with st.spinner("O Gemini está analisando..."):
                try:
                    # --- OTIMIZAÇÃO PARA O RENDER ---
                    # Copia a imagem e redimensiona para no máximo 1080px (mantendo a proporção)
                    img_otimizada = imagem_original.copy()
                    img_otimizada.thumbnail((1080, 1080))
                    
                    # Converte para RGB se for PNG (evita erros de transparência)
                    if img_otimizada.mode in ('RGBA', 'P'):
                        img_otimizada = img_otimizada.convert('RGB')
                    
                    # Salva em um buffer de memória comprimindo como JPEG (Qualidade 80% reduz drasticamente o peso)
                    buffer = io.BytesIO()
                    img_otimizada.save(buffer, format="JPEG", quality=80)
                    imagem_bytes = buffer.getvalue()
                    # ---------------------------------

                    prompt = """
                    Você é um especialista em fisiculturismo,
                    biomecânica e avaliação estética desportiva.

                    Analise a foto fornecida e retorne um relatório
                    estruturado em Markdown com:

                    1. Estimativa visual do percentual de gordura corporal.
                    2. Avaliação de simetria e proporção muscular.
                    3. Principais pontos fortes estéticos visíveis.
                    4. Grupos musculares que poderiam receber maior foco.

                    Seja profissional, motivador e técnico.
                    Deixe claro que a estimativa de percentual de gordura
                    é apenas visual e não uma medição clínica.
                    """

                    # Forma correta e nativa aceita pelo SDK google-genai para o Pillow
                    resposta = client.models.generate_content(
                        model="gemini-3.6-flash",
                        contents=[prompt, img_otimizada]
                    )


                    st.success("Análise concluída!")
                    st.subheader("📝 Relatório da IA")
                    st.markdown(resposta.text)

                except Exception as e:
                    if "503" in str(e):
                        st.error("⚠️ Os servidores do Google estão lotados agora (Erro 503). Por favor, clique no botão novamente para tentar uma nova requisição.")
                    else:
                        st.error(f"Erro ao chamar a API do Gemini: {e}")
else:
    st.info("Aguardando o envio de uma foto.")
