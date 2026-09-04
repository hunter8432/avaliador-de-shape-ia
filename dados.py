import pandas as pd

def carregar_dados():
    dados = {
        'Mês':['Janeiro','Fevereiro','Março','Abril','Maio'],
        'Exercicio':['Remada alta','Puxada aberta','Rosca W','Puxada Supinada','Abdominal'],
        'Peso corporal':[75,76.5,77.2,77.5,78],
        'Carga dos Exercicios':[80,85,30,80,50],
        'Medida corporais':[45,50,40,60,48],
        'Corpo':['Biceps','Quadril','Triceps','Ombro','Perna']
    }
    return pd.DataFrame(dados)