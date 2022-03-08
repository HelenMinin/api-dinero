import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'A API está ativa!!!'

@app.route('/pegarvendas')
def pegar_vendas():
    tabela = pd.read_csv('12-18 - Criando API no Python.csv')
    total_vendas = tabela['Vendas'].sum()
    resposta = {'Total_vendas': total_vendas}
    return resposta

app.run()