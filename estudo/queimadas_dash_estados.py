# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 03:18:04 2021

@author: Eduardo
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.express as px
import json
import dash_table
from dash_table.Format import Format, Group, Scheme, Symbol

df = pd.read_csv('dataset/historico_bioma_estados.csv', encoding='latin-1')

with open('dataset/estados_brasil.geojson') as data:
    limites_brasil = json.load(data)
    
for feature in limites_brasil ['features']:
    feature['id'] = feature['properties']['name']
    
fig = px.choropleth_mapbox(
    df,
    locations = 'UF',
    geojson = limites_brasil,
    color = 'Total',
    mapbox_style="carto-positron",
    center = {'lon':-55, 'lat':-14},
    zoom =3,
    #opacity = 0.5,
    hover_data = { 'UF': False},
    hover_name= "UF",
    color_continuous_scale='reds',
    range_color = [0, df['Total'].max()],
    # animation_frame = "Ano"
    )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
pyo.offline.plot(fig,filename='mapa-01.html')