import dash
import pandas as pd
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Output,Input
from dash import dash_table
from plotly.subplots import make_subplots
import requests

response1 = requests.get('http://fastapi:8000/streaming/?start=1&end=946', headers={'accept': 'application/json'})
response2 = requests.get('http://fastapi:8000/historical/?start=1&end=2335', headers={'accept': 'application/json'})
data1 = response1.json()
data2 = response2.json()
df_streaming = pd.DataFrame(data1['data'])
df_historical = pd.DataFrame(data2['data'])
df_streaming['open_time'] = pd.to_datetime(df_streaming['open_time'])
df_historical['open_time'] = pd.to_datetime(df_historical['open_time'])
fig1 = px.line(df_streaming, x='open_time', y='close_price', title='Streaming Data Bitcoin')
fig2 = px.line(df_historical, x='open_time', y='close_price', title='Historical Data Bitcoin')



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
        html.H2('Charts'),
        #html.Pre(children=str(df))
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2)
    ])

if __name__ == '__main__':
    app.run_server(debug=True,host="0.0.0.0")


