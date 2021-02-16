# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 02:27:54 2021

@author: Mariot
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
     dcc.Input(id='input-1', type='text', value='Curitiba'),
     dcc.Input(id='input-2', type='text', value='Foz do Iguaçu'),
     html.Button(id='submit-state', n_clicks=0, children='Submit'),
     html.Div(id='output-state')
    ])

@app.callback(
    Output('output-state', 'children'),
    Input('submit-state', 'n_clicks'),
    State('input-1', 'value'),
    State('input-2', 'value'),
    )
def update_output(n_clicks,input1, input2):
    return u'''The Button has been pressed {} times,
                Input 1 is "{}",
                Input 2 is "{}"'''.format(n_clicks, input1, input2)

if __name__ == "__main__":
    app.run_server(debug=True)