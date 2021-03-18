# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Leitura dos dados

df = pd.read_csv('dataset/historico_bioma.csv', encoding='latin-1')

# Criando uma variável para armazenar os estados

biome_options = []
for biome in df['Bioma'].unique():
    biome_options.append({'label': biome, 'value': biome})

app.layout = html.Div([
    
    # Cabeçalho
    
    html.Div([
        
        # Título
        
        html.H1("Dados de focos de queimadas por Bioma no Brasil entre 1998 e 2020",
            style = {
                'textAlign':'center',
                'fontFamily': 'Roboto',
                'paddingTop':20
                
                }
            
            ),
        
       
       # Dropdown
       
        html.Div([
            html.Label("Selecione um bioma: "),
            dcc.Dropdown(
                id='biome-picker',
                 options = biome_options,
                 value='Amazônia',
                 clearable=False
                 ),
      
        
        ], style={'width': '33%',
                  'display':'inline-block'}),
     
       # Gráfico Dispersão
       
       html.Div([
           
           # Título do Gráfico
           
           html.H3(id='titulo-scatter',
                   style={
                       'textAlign': 'center',
                       'fontFamily': 'Roboto',
                       'paddingTop': 15
                       }
                   ),
           # Gráfico de disperção
           dcc.Graph(
               id='scatter-plot'
               )
           
           ], style={
               'paddingLeft': '10%',
               'paddingRight': '10%',
               'width': '80%',
               'display':'inline-black'
               }),
       
       # Gráfico de Barra
       
       html.Div([
           
           # Título do Gráfico
           
           html.H3(id='titulo-barplot',
                   style={
                       'textAlign': 'center',
                       'fontFamily': 'Roboto',
                       'paddingTop': 10
                       }
                   ),
           # Gráfico de barras
           dcc.Graph(
               id='bar-plot'
               )
           
           ], style={
               'paddingLeft': '10%',
               'paddingRight': '10%',
               'width': '80%',
               'display':'inline-black'
               })
            
       
        ])
    ])

# Atualiza o título do gráfico de dispersão                  
@app.callback(Output('titulo-scatter', 'children'),
              [Input('biome-picker', 'value')])
def update_title_scatter(selected_biome):
    return "Número de focos de queimadas por mês no bioma: " + str(selected_biome)

# Atualiza o título do gráfico de barras                  
@app.callback(Output('titulo-barplot', 'children'),
              [Input('biome-picker', 'value')])
def update_title_barplot(selected_biome):
    return "Número TOTAL de focos de queimadas por ano durante todo o período no bioma: " + str(selected_biome)

# Atualiza o gráfico de dispersão 
@app.callback(Output('scatter-plot', 'figure'),
              [Input('biome-picker', 'value')])
def update_scatter(selected_biome):
    df_aux = df[df['Bioma']==selected_biome]
    df_aux.reset_index(drop=True, inplace=True)
    
    tr = []
    for i in range(df_aux.shape[0]):
        tr.append(go.Scatter(
            x=df_aux.columns.values[1:13],
            y=df_aux.loc[i][1:13],
            mode = 'lines+markers',
            name= str(df_aux['Ano'][i]),
            hovertemplate=df_aux.columns.values[1:13] + ' de ' + str(df_aux['Ano'][i]) 
            + '<br>nº de focos: ' + [str(i) for i in list(df_aux.loc[i][1:13])]
            ))
    
    return{
        'data':tr,
        'layout': go.Layout(
            showlegend=True,
            hovermode='closest',
            hoverlabel=dict(
                bgcolor="white",
                font_size=16,
                font_family="Roboto"
                ),
            xaxis=dict(title='Meses', linecolor='rgba(0,0,0,1)'),
            yaxis=dict(title='Número de focos de queimadas', linecolor='rgba(0,0,0,1)')
            
            )
        }            

# Atualiza o gráfico de barras
@app.callback(Output('bar-plot', 'figure'),
              [Input('biome-picker', 'value')])
def update_bar_plot(selected_biome):
    df_aux = df[df['Bioma']==selected_biome]
    df_aux.reset_index(drop=True, inplace=True)
    
    tr =[go.Bar(
        x=df_aux['Ano'],
        y=df_aux['Total'],
        name = selected_biome,
        hovertemplate=['Total de focos de queimadas: ' + i for i in [str(i) for i in (df_aux['Total'])]],
        )]
    return{
        'data': tr,
        'layout': go.Layout(
            xaxis = dict(title = 'Anos', linecolor='rgba(0,0,0,1)', tickmode='array', tickvals= df_aux['Ano'], ticktext=df_aux['Ano']),
            yaxis = dict(title ='Total de queimadas por ano', linecolor='rgba(0,0,0,1)', tickformat=False),
            showlegend=True,
            hoverlabel=dict(bgcolor='white',
                            font_size=16,
                            font_family='Roboto')
            
            )
        
        }

if __name__ == '__main__':
    app.run_server(debug=True) 