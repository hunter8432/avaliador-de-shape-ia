import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def criar_dashboard(df):

    fig = make_subplots(
        rows=1,
        cols=2,
        subplot_titles=(
            "Peso corporal",
            "Carga dos Exercícios"
        )
    )

    fig.add_trace(
        go.Bar(
            x=df['Mês'],
            y=df['Peso corporal']
        ),
        row=1,
        col=1
    )

    fig.add_trace(
        go.Bar(
            x=df['Exercicio'],
            y=df['Carga dos Exercicios']
        ),
        row=1,
        col=2
    )

    return fig
