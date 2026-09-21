import streamlit as st


def show_analysis_result(response):
    st.success("Análise concluída!")
    st.subheader("📝 Relatório da IA")
    st.markdown(response.text)