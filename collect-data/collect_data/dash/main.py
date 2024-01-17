import dash
import pandas as pd
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Output, Input, State
from dash import dash_table
from plotly.subplots import make_subplots
import requests

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.H1('Kryptobot', style={'color': 'black', 'textAlign': 'center'}),
    html.Hr(style={'borderWidth': "0.5vh", "width": "100%", "borderColor": "#F3DE8A", "opacity": "unset"}),
    html.Div([
        html.Button('Refresh Data', id='refresh-button', n_clicks=0),
        html.Div(id='refresh-output'),
        html.Button('Show Prediction', id='prediction-button', n_clicks=0)
    ]),
    html.Div(id='page-content'),
    html.Hr(style={'borderWidth': "0.5vh", "width": "100%", "borderColor": "#F3DE8A", "opacity": "unset"})
])


def get_data():
    response1 = requests.get('http://fastapi:8000/streaming_raw', headers={'accept': 'application/json'})
    response2 = requests.get('http://fastapi:8000/historical_raw', headers={'accept': 'application/json'})
    data1 = response1.json()
    data2 = response2.json()
    df_streaming = pd.DataFrame(data1['data'])
    df_historical = pd.DataFrame(data2['data'])
    df_streaming['open_time'] = pd.to_datetime(df_streaming['open_time'])
    df_historical['open_time'] = pd.to_datetime(df_historical['open_time'])
    fig1 = px.line(df_streaming, x='open_time', y='close_price', title='Streaming Data Bitcoin')
    fig2 = px.line(df_historical, x='open_time', y='close_price', title='Historical Data Bitcoin')
    return fig1, fig2


@app.callback([Output('page-content', 'children'),
               Output('refresh-output', 'children')],
              [Input('url', 'pathname'),
               Input('refresh-button', 'n_clicks')],
              prevent_initial_call=True)
def display_page(pathname, n_clicks):
    if n_clicks > 0:
        fig1, fig2 = get_data()
        return html.Div([
            html.H2('Charts'),
            dcc.Graph(figure=fig1),
            dcc.Graph(figure=fig2)
        ]), 'Data refreshed successfully!'
    else:
        fig1, fig2 = get_data()
        return html.Div([
            html.H2('Charts'),
            dcc.Graph(figure=fig1),
            dcc.Graph(figure=fig2)
        ]), ''


if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")
