import dash
import pandas as pd
from dash import dcc
import numpy as np
from dash import html
import plotly.express as px
from dash.dependencies import Output, Input, State
from dash import dash_table
from plotly.subplots import make_subplots
import requests
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import psycopg2
from sqlalchemy.engine import URL
from sqlalchemy.inspection import inspect
from sqlalchemy import create_engine, Table, MetaData, insert, Column, DateTime, Float
from datetime import timedelta


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

def predict_price():
    historical = requests.get('http://fastapi:8000/historical_raw', headers={'accept': 'application/json'})
    data_historical = historical.json()
    df_ml = pd.DataFrame(data_historical['data'])

    X = df_ml[['volume', 'number_of_trades']]
    y = df_ml['close_price']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the machine learning model
    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    # Make predictions for the next 30 days
    df_ml['close_time'] = pd.to_datetime(df_ml['close_time'])
    future_dates = pd.date_range(df_ml['close_time'].max() + timedelta(days=1), periods=30, freq='D')

    latest_data = df_ml.iloc[-1]
    future_features = pd.DataFrame(columns=['volume', 'number_of_trades'])

# Populate future_features with the latest values
    for col in future_features.columns:
        future_features[col] = [latest_data[col]] * 30
    
    future_predictions = model.predict(future_features)

    # Save predictions to the PostgreSQL database
    save_to_database(future_dates, future_predictions)

    return future_dates, future_predictions


# Function to save predictions to the PostgreSQL database
def save_to_database(dates, predictions):
    # Convert numpy.ndarray to a list
    predictions = predictions.tolist()

    # Convert DatetimeIndex to a list of datetime objects and then to a list of strings
    dates_str = pd.to_datetime(dates).strftime('%Y-%m-%d %H:%M:%S').tolist()

    # Create a DataFrame with the data
    data_to_insert = pd.DataFrame({'date': dates_str, 'prediction': predictions})

    # Connect to the PostgreSQL database
    url = "postgresql://postgres:123456@db/opa_binance"
    engine = create_engine(url, pool_pre_ping=True)

    # Check if the 'predictions' table exists
    inspector = inspect(engine)
    if not inspector.has_table('predictions'):
        metadata = MetaData()
        predictions_table = Table('predictions', metadata,
            Column('date', DateTime(timezone=False)),  # Specify timezone=False for timestamp without time zone
            Column('prediction', Float)
        )
        metadata.create_all(engine)  # Create the table if it doesn't exist

    # Insert the data into the 'predictions' table
    try:
        data_to_insert.to_sql('predictions', con=engine, index=False, if_exists='append')
        print("Insert successful.")
    except Exception as e:
        print(f"Insert failed with error: {e}")



def get_data():
    response1 = requests.get('http://fastapi:8000/streaming_raw', headers={'accept': 'application/json'})
    response2 = requests.get('http://fastapi:8000/historical_raw', headers={'accept': 'application/json'})
    data1 = response1.json()
    data2 = response2.json()
    df_streaming = pd.DataFrame(data1['data'])
    df_historical = pd.DataFrame(data2['data'])
    df_streaming['open_time'] = pd.to_datetime(df_streaming['close_time'])
    df_historical['open_time'] = pd.to_datetime(df_historical['close_time'])
    fig1 = px.line(df_streaming, x='close_time', y='close_price', title='Streaming Data Bitcoin')
    fig2 = px.line(df_historical, x='close_time', y='close_price', title='Historical Data Bitcoin')
    return fig1, fig2


@app.callback([Output('page-content', 'children'),
               Output('refresh-output', 'children')],
              [Input('url', 'pathname'),
               Input('refresh-button', 'n_clicks'),
               Input('prediction-button', 'n_clicks')],
              prevent_initial_call=True)

def display_page(pathname, refresh_clicks, prediction_clicks):
    if refresh_clicks > 0 or prediction_clicks > 0:
        fig1, fig2 = get_data()
        
        if prediction_clicks > 0:
            # Assuming df_historical is the historical dataframe used for predictions
            future_dates, future_predictions = predict_price()
            
            # Display the predicted values
            prediction_output = html.Div([
                html.H2('Predictions for the Next 30 Days'),
                dcc.Graph(figure=px.line(x=future_dates, y=future_predictions, title='Predicted Prices'))
            ])
            
            return [html.Div([
                        html.H2('Charts'),
                        dcc.Graph(figure=fig1),
                        dcc.Graph(figure=fig2),
                        prediction_output
                    ]), 'Data refreshed successfully!']
        else:
            return [html.Div([
                        html.H2('Charts'),
                        dcc.Graph(figure=fig1),
                        dcc.Graph(figure=fig2)
                    ]), 'Data refreshed successfully!']
    else:
        fig1, fig2 = get_data()
        return [html.Div([
                    html.H2('Charts'),
                    dcc.Graph(figure=fig1),
                    dcc.Graph(figure=fig2)
                ]), '']
if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")
