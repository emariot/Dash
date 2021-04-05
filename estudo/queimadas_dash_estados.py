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
    
# Carregando dados de Geolocalização
with open('dataset/estados_brasil.geojson') as response:
    limites_brasil = json.load(response)
for features in limites_brasil['features']:
    features['id'] = features['properties']['name']    

app = dash.Dash(external_stylesheets=[boot.themes.BOOTSTRAP, boot.themes.GRID])

app.layout = html.Div([ # Div Geral
    html.Div(# Div para o modal
        boot.Modal([
                boot.ModalHeader("Aviso!", 
                                 style= {'color':'red'}),
                boot.ModalBody([
                   html.Label("O mapa do Brasil pode demorar alguns segundos a mais para atualizar do que os demais gráficos em alguns navegadores."), 
                   html.Br(),
                   html.Label("Pedimos desculpas pelo incoveniênte!"),
                   html.Label("\U0001F605")
                    ]),
                boot.ModalFooter(
                    boot.Button(
                        "Ok!",
                        id="close-sm",
                        className="ml-auto"
                        )
                    )
                
                ], id = 'modal', is_open = True, centered = True, style={'textAlign':'center'}
                    
                )        
             ), 
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
                    
                    ), style = {'paddingTop': "5px",
                                'paddingBottom': '10px',
                                'paddingLeft': '10%'}
                ), 
            boot.Row( #Mapa + Tabela
                [
                    boot.Col( #Mapa
                        dcc.Graph(id='map-brazil'),
                        width = 7,
                        align = 'center',
                        style = {
                            'display': 'inline-block',
                            'paddingLeft': '2%',
                            'paddingRight': '2%',
                            }
                        ),
                    boot.Col( #Tabela       
                        html.Div(id = 'mapa-data-table'),
                                 width = 5,
                                 align ='center',
                                 style = {
                                     'display': 'inline-block',
                                     'paddingLeft': '2%',
                                     'paddingRight': '2%'
                                     }
                            
                    
                        ),    
                    ]
                
                ), 
            
            ]
        ), 
    html.Div(), # Dados Separados por região
    html.Div(), # Dados separados por Estados
    html.Div(), # Footer
    ])
                                                 
                                
# Função para atualizar a tabela do mapa quando o usuário alterar o dropdown
@app.callback(Output('mapa-data-table', 'children'),
              [Input('year-picker', 'value')])
def update_table_map(selected_year):
    df_ano = df[df['Ano']==selected_year]
    df_ano = df_ano.drop(['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro',
                'Dezembro', 'Ano'], axis=1)
    df_ano.sort_values(by='Total', inplace=True, ascending=False)
    df_ano.reset_index(inplace=True, drop=True)
    df_ano['Rank'] = df_ano.index
    df_ano['Rank'] = df_ano['Rank'] + 1
    df_ano = df_ano[['Rank', 'Total', 'UF', 'Regiao']]

    return[
       
       dash_table.DataTable(
           columns=[{"name": i, "id": i} for i in df_ano.columns],
           data = df_ano.to_dict('records'),
           fixed_rows={'headers': True},
           style_table={'height':'400px', 'overflowY': 'auto'},
           style_header={'textAlign':'center'},
           style_cell={'textAlign': 'center', 'font-size': '14px'},
           style_as_list_view=True,
           style_data_conditional=[
               {
                   "if": {"state": "selected"},
                   "backgroundColor": "rgba(205, 205, 205,0.3)",
                   "border": "inherit !important"
                   
                   }
               
               ],
           
           )
       
       ]
                                
# Função para atualizar o mapa quando o usuário alterar o dropdown
@app.callback(Output('map-brazil', 'figure'),
              [Input('year-picker', 'value')])
def update_map_brazil(selected_year):
    df_ano = df[df['Ano']==selected_year]
    
    # Criando o mapa
    fig = px.choropleth_mapbox(
                                df_ano,
                                locations = 'UF',
                                geojson = limites_brasil,
                                color = 'Total',
                                mapbox_style= "carto-positron",
                                center = {'lon':-55, 'lat':-14},
                                zoom = 3,
                                opacity = 1.0,
                                hover_name = 'UF',
                                color_continuous_scale='reds',
                                range_color = [0, df['Total'].max()]
                                )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    
    return fig

# Modal                                
@app.callback(Output('modal', 'is_open'),
              [Input('close-sm', 'n_clicks')],
              [State('modal', 'is_open')])
def close_modal(n, is_open):
    if n:
        return not is_open
    return is_open

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






