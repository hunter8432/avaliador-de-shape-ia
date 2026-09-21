import streamlit as st


def get_api_key_input(api_key):
    if api_key:
        return api_key

    return st.text_input(
        "Insira sua Gemini API Key:",
        type="password"
    ).strip()