# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 01:57:29 2021

@author: Mariot
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

all_options = {
    'Paraná': ['Curitiba', 'Maringá', 'Foz do Iguaçú'],
    'Santa Catarina': ['Florianópolis', 'Criciúma', 'Itajaí']
    }

app.layout = html.Div([
    dcc.RadioItems(
        id='estado-radio',
        options=[{'label':k,'value':k}for k in all_options.keys()],
        value='Paraná'
        ),
    html.Hr(),
    dcc.RadioItems(id='cidade-radio'),
    html.Hr(),
    html.Div(id='display-selected-values')
    
    ])

@app.callback(
    Output('cidade-radio', 'options'),
    Input('estado-radio', 'value'))
def set_cities_options(selected_estado):
    return [{'label':i, 'value':i} for i in all_options[selected_estado]]

@app.callback(
    Output('cidade-radio', 'value'),
    Input('cidade-radio', 'options'))
def set_cities_value(available_options):
    return available_options[0]['value']

@app.callback(
    Output('display-selected-values', 'children'),
    Input('estado-radio', 'value'),
    Input('cidade-radio', 'value'))
def set_display_children(selected_estado, selected_cidade):
    return f'{selected_estado} is a city in {selected_cidade}'


if __name__ == '__main__':
    app.run_server(debug=True)