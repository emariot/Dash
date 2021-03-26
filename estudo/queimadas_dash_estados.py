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
                     html.H3('Total de focos de queimadas identificados por Estado no ano de XXXX')
                     ), style={'textAlign':'center',
                               'paddingTop':'40px',
                               'paddingBottom':'40px'}
                ), 
            boot.Row(), # Texto + Popover
            boot.Row(), # Dropdown
            boot.Row(), # Mapa + Tabela
            
            ]
        ), 
    html.Div(), # Dados Separados por região
    html.Div(), # Dados separados por Estados
    html.Div(), # Footer
    ])


if __name__ == '__main__':
    app.run_server(debug = True, use_reloader = True)