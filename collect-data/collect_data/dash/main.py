import dash
import pandas as pd
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Output,Input
from dash import dash_table
from plotly.subplots import make_subplots
import requests

response = requests.get('http://localhost:8000/streaming/', headers={'accept': 'application/json'})
data = response.json()
df = pd.DataFrame(data['data'])
df['open_time'] = pd.to_datetime(df['open_time'])
fig = px.line(df, x='open_time', y='close_price', title='Close Price Over Time')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.H1('Kryptobot', style={'color' : 'black', 'textAlign': 'center'}),
    html.Hr(style={'borderWidth': "0.5vh", "width": "100%", "borderColor": "#F3DE8A","opacity": "unset"}),
    html.Div(id = 'page-content'),
    html.Hr(style={'borderWidth': "0.5vh", "width": "100%", "borderColor": "#F3DE8A","opacity": "unset"})
])




@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
                      
def display_page(pathname):
    return html.Div([
        html.H2('Streaming Data for BTC-USD'),
        #html.Pre(children=str(df))
        dcc.Graph(figure=fig)
    ])

if __name__ == '__main__':
    app.run_server(debug=True,host="0.0.0.0")


