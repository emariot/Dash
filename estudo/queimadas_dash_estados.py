# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 03:18:04 2021

@author: Eduardo
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as boot
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.express as px
import json
import dash_table
from dash_table.Format import Format, Group, Scheme, Symbol

df = pd.read_csv('dataset/historico_bioma_estados.csv', encoding='latin-1')

year_options = []
for ano in df['Ano'].unique():
    year_options.append({'label':str(ano), 'value': ano})

app = dash.Dash()
app = dash.Dash(external_stylesheets=[boot.themes.BOOTSTRAP, boot.themes.GRID])

app.layout = html.Div([
    html.Div( # Título Geral
        boot.Row(
            boot.Col(
                html.H3("Histórico de queimadas no Brasil entre 1998 e 2020.")
                
                ), style = {
                    'textAlign': 'center',
                    'color': 'blue'
                    }
            ), style = {
                'paddingTop': '20px',
                'paddingBotton': '20px'
                }
        ), 
    html.Div( # Dados do Mapa
        [
            boot.Row( # Título
                 boot.Col(
                     html.H3(id='title-year')
                     ), style={'textAlign':'center',
                               'paddingTop':'40px',
                               'paddingBottom':'40px'}
                ), 
            boot.Row(), # Texto + Popover
            boot.Row( # Dropdown
                boot.Col(
                    dcc.Dropdown(
                        id = 'year-picker',
                        value = 2020,
                        options = year_options,
                        clearable = False,
                        style = {'width': '50%'}
                        ),
                    
                    ), style = {'paddinfTop': "5px",
                                'paddingBottom': '10px',
                                'paddingLeft': '10%'}
                ), 
            boot.Row(), # Mapa + Tabela
            
            ]
        ), 
    html.Div(), # Dados Separados por região
    html.Div(), # Dados separados por Estados
    html.Div(), # Footer
    ])
            
@app.callback(Output('title-year', 'children'),
              [Input('year-picker', 'value')])
def update_mape(selected_year):
    return "Total de focos de queimadas identificados por estado no ano de " + str(selected_year)

if __name__ == '__main__':
    app.run_server(debug = True, use_reloader = True)