# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 01:51:12 2021

@author: Mariot
"""

import dash
import dash_core_components as doc
import dash_html_components as html
import pandas as pd

colors= {
    "background": '#111111',
    'text': "#7FDBFF"
    }


df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

def generate_table(df, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in df.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
                ]) for i in range(min(len(df), max_rows))
            ])
     
        ])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(style={
    'backgroundColor':colors['background']
    
    },children=[
    
    html.H4('US Agriculture Exports (2011)', style={
        'textAlign':'center',
        'color':colors['text']}),
    generate_table(df)
    
    ])

if __name__ == '__main__':
    app.run_server(debug=True)