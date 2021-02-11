# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 02:03:40 2021

@author: Mariot
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

markdown_text = '''### Expectativa de vida
Esperança de vida, esperança de vida à nascença, esperança de vida ao nascer ou expectativa de vida é o número aproximado de anos que um grupo 
de indivíduos nascidos no mesmo ano irá viver, se mantidas as mesmas condições desde o seu nascimento.
Em outras palavras, a expectativa de vida é uma medida estatística da média de tempo de vida de um organismo, 
com base no ano de seu nascimento, sua idade atual e outros fatores demográficos, incluindo sexo.
'''

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

fig = px.scatter(df,
                 x="gdp per capita",
                 y="life expectancy",
                 size="population",
                 color="continent",
                 hover_name="country",
                 log_x=True, size_max=60
                 )
app.layout = html.Div(children=[
    
    html.H1('Life Expctancy by income', style={
        'textAlign':'center',
        }),
    html.Div(
        dcc.Markdown(markdown_text, style={
            'textAlign':'center'
            })
        ),
    html.Div('Data: GitHub', style={
        'textAlign':'center'
        }),
    dcc.Graph(
        id="life-exp-vc-dgp",
        figure=fig
        )
    
    ])


if __name__ =='__main__':
    app.run_server(debug=True)