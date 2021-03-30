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
df_texto_ano = pd.read_csv('dataset/info-anos.csv',  encoding='latin-1', sep=';')

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
            boot.Row( # Texto + Popover
                     [
                     
                    boot.Col( # Texto
                        html.Label("Escolha um ano:"),
                        width = 3,
                        align = 'left',
                        style={'display':'inline-block'}
                        ),
                    boot.Col( # Popover
                        html.Div(
                            [
                                boot.Button(
                                    "+ info",
                                    outline = True,
                                    id = 'popovertarget-mapa',
                                    style = {
                                        'fontFamily': 'Garamond'
                                        },
                                    className='mr-2',
                                    color='success',
                                    size='sm'
                                    ),
                                boot.Popover(
                                    [
                                    boot.PopoverHeader(id='popover-header-mapa'),
                                    boot.PopoverBody(
                                        dcc.Markdown(
                                            id='popover-body-mapa',
                                            style={
                                                'textAlign':'justify'
                                                }
                                            ),style={
                                                'overflow': 'auto',
                                                'max-height': '500px'
                                                }
                                    
                                        )
                                    
                                    ],
                                    id ='popover-mapa',
                                    target='popovertarget-mapa',
                                    placement='bottom-end',
                                    is_open = False
                                    
                                    ),
                                
                                ]
                            ),
                            width = 2,
                            align = 'right'
                                    
                        )
                         ], style = {'paddingLeft': '12%', 'paddingRight': '5%'},
                            justify='between'
                     
                     ),
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

# Header para o popover do mapa
@app.callback(Output('popover-header-mapa', 'children'),
              [Input('year-picker', 'value')])
def update_pop_over_header_mapa(selected_year):
    return "Brasil em "+str(selected_year)
                                
# Conteúdo do corpo para o popover do mapa                                
@app.callback(Output('popover-body-mapa', 'children'),
              [Input('year-picker', 'value')])
def update_pop_over_body_mapa(selected_year):
    return df_texto_ano[df_texto_ano['Ano'] == selected_year]['Texto']                   
            
# Alterando o estado do popover, de False para True, de True para False ao clicar
@app.callback(Output("popover-mapa", "is_open"),
              [Input('popovertarget-mapa', "n_clicks")],
              [State("popover-mapa", "is_open")])
def toggle_popover_mapa(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(Output('title-year', 'children'),
              [Input('year-picker', 'value')])
def update_mape(selected_year):
    return "Total de focos de queimadas identificados por estado no ano de " + str(selected_year)

if __name__ == '__main__':
    app.run_server(debug = True, use_reloader = True)