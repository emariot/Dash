# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    
    html.Div([
        
        html.H1("Dados de focos de queimadas por Bioma no Brasil entre 1998 e 2020",
            style = {
                'textAlign':'center',
                'fontFamily': 'Roboto',
                'paddingTop':20
                
                }
            
            ),
        
        html.P("Selecione um bioma: ", style={'fontFamily':'Roboto'}),
        
        html.Div([
         dcc.Dropdown(
             id='biome-picker',
             value='Amazônia',
             options = [{'label': 'Amazônia', 'value':0},
                        {'label': 'Pampa', 'value':1},
                        {'label': 'Pantanal', 'value':2}]
             ) 
        
        ], style={'width': '33%',
                  'display':'inline-block'})
     
        
        ])
    ])


if __name__ == '__main__':
    app.run_server(debug=True) 