import streamlit as st

from services.image_services import optimize_image
from services.gemini_services import analyze_shape
from prompt.shape_prompt import SHAPE_PROMPT
from config.settings import get_gemini_api_key
from components.image_uploads import upload_image
from components.resultado import show_analysis_result
from components.api_key_input import get_api_key_input


st.set_page_config(
    page_title="Avaliador de Shape",
    page_icon="💪",
    layout="centered"
)

st.title("💪 Avaliador de Shape com Inteligência Artificial")


api_key = get_api_key_input(get_gemini_api_key())

if not api_key:
    st.warning("⚠️ Configure sua Gemini API Key.")
    st.stop()


st.subheader("📸 Envie a foto do seu Shape")

imagem_original = upload_image()


if imagem_original is not None:

    if st.button("🚀 Analisar Shape com IA Real"):

        with st.spinner("O Gemini está analisando..."):

            try:
                imagem_otimizada = optimize_image(imagem_original)

                resposta = analyze_shape(
                    api_key,
                    imagem_otimizada,
                    SHAPE_PROMPT
                )

                show_analysis_result(resposta)

            except Exception as e:
                st.error(str(e))

else:
    st.info("Aguardando o envio de uma foto.")