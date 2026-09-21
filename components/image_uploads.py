import streamlit as st
from PIL import Image


def upload_image():
    foto_enviada = st.file_uploader(
        "Escolha uma imagem",
        type=["jpg", "jpeg", "png"]
    )

    if foto_enviada is None:
        return None

    imagem_original = Image.open(foto_enviada)

    st.image(
        imagem_original,
        caption="Foto carregada com sucesso!",
        use_container_width=True
    )

    return imagem_original