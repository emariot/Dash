import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


colors= {
    "background": '#111111',
    'text': "#7FDBFF"
    }

d = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 15],
    "City": ["SF", "SF", "SF", "Curitiba", "Curitiba", "Curitiba"]
})

fig = px.bar(d, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
    )

app.layout = html.Div(style={
    'backgroundColor':colors['background']
    
    },children=[
    html.H1('Hello Dash',
    style={
        'textAlign':'center',
        'color':colors['text']
        
        }
),
    html.Div('Dash: A web application framework for Python.',
             style={
                 'textAlign':'center',
                 'color':colors['text']
                 
                 
                 }
             ),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)