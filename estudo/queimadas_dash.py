# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

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
            
                 options = [{'label': 'Amazônia', 'value':'Amazônia'},
                            {'label': 'Pampa', 'value':'Pampa'},
                            {'label': 'Pantanal', 'value':'Pantanal'}],
                 value='Amazônia',
                 ),
      
        
        ], style={'width': '33%',
                  'display':'inline-block'}),
     
       # Gráfico
       
       html.Div([
           
           # Título do Gráfico
           
           html.H3(id='titulo-scatter',
                   style={
                       'textAlign': 'center',
                       'fontFamily': 'Roboto',
                       'paddingTop': 15
                       }
                   )
           
           ])
       
        ])
    ])

# Atualiza o título do gráfico de dispersão                  
@app.callback(Output('titulo-scatter', 'children'),
              [Input('biome-picker', 'value')])
def update_title_scatter(selected_biome):
    return "Número de focos de queimadas por mês no bioma: " + str(selected_biome)
                  


if __name__ == '__main__':
    app.run_server(debug=True) 