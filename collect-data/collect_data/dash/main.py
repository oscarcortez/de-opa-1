import dash
import pandas as pd
from dash import html, dcc
from dash import dash_table
import plotly.express as px
from dash.dependencies import Output, Input
import requests
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import psycopg2
from sqlalchemy.engine import URL
from sqlalchemy.inspection import inspect
from sqlalchemy import create_engine, Table, MetaData, insert, Column, DateTime, Float
from datetime import timedelta
from statsmodels.tsa.arima.model import ARIMA

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.H1('Kryptobot DE_OPA_1', style={'color': 'black', 'textAlign': 'center'}),
    html.Hr(style={'borderWidth': "0.5vh", "width": "100%", "borderColor": "#F3DE8A", "opacity": "unset"}),
    html.Div([
        html.Button('Refresh Data', id='refresh-button', n_clicks=0),
        html.Button('Show Prediction', id='prediction-button', n_clicks=0),
        html.Div(id='refresh-output'),
        dcc.Store(id='button-clicks', data={'refresh': 0, 'prediction': 0})
    ]),
    html.Div(id='page-content'),
    html.Hr(style={'borderWidth': "0.5vh", "width": "100%", "borderColor": "#F3DE8A", "opacity": "unset"})
])

def predict_price():
    # Fetch historical data from the API
    historical = requests.get('http://fastapi:8000/historical_raw', headers={'accept': 'application/json'})
    data_historical = historical.json()
    df = pd.DataFrame(data_historical['data'])

    # Extract relevant columns and convert to datetime
    df_ml = df[['close_time', 'close_price']]
    df_ml['close_time'] = pd.to_datetime(df_ml['close_time'])
    df_ml['close_price'] = df_ml['close_price'].astype(float)
    df_ml.set_index('close_time', inplace=True)

    # Fit ARIMA model
    model = ARIMA(df_ml, order=(5, 1, 2))
    results = model.fit()

    # Get the last 10 days of historical data
    last_10_days = df_ml.index[-10:]
    historical_data = df_ml.loc[last_10_days]

    # Get forecast values for the next 30 days
    forecast_values = results.get_forecast(steps=30)
    forecast_data = forecast_values.predicted_mean.to_frame(name='yhat')
    future_dates = pd.date_range(last_10_days[-1] + timedelta(days=1), periods=30, freq='D')
    future_predictions = forecast_data['yhat'].values

    # Save predictions to the PostgreSQL database
    save_to_database(future_dates, future_predictions)

    # Create a plot for the last 10 days and predictions
    prediction_figure = px.line()
    prediction_figure.add_scatter(x=last_10_days, y=historical_data['close_price'].values, mode='lines', name='Historical', line=dict(color='blue'))
    prediction_figure.add_scatter(x=future_dates, y=future_predictions, mode='lines', name='Prediction', line=dict(color='green'))
    prediction_figure.update_layout(title='Historical Prices and Predicted Prices', xaxis_title='Date', yaxis_title='Price')

    # Create a DataTable for displaying the data
    data_table = pd.concat([historical_data, pd.Series(future_predictions, index=future_dates)], axis=1)
    data_table.columns = ['Historical Prices', 'Predicted Prices']
    data_table.reset_index(inplace=True)

    return last_10_days, historical_data, prediction_figure, data_table




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
    if inspector.has_table('predictions'):
        # If the table exists, drop it
        with engine.connect() as connection:
            table = Table('predictions', MetaData(), autoload_with=connection)
            table.drop(engine)

        print("Table 'predictions' dropped.")

    # Create the 'predictions' table
    metadata = MetaData()
    
    metadata.create_all(engine)

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
    fig1, fig2 = get_data()
    output_message = ''

    if refresh_clicks is None and prediction_clicks is None:
        # Initial load or no button clicked
        return [html.Div([
                    html.H2('Charts with historical data and streaming data'),
                    dcc.Graph(figure=fig1),
                    dcc.Graph(figure=fig2)
                ]), '']

    ctx = dash.callback_context
    button_id = ctx.triggered_id

    if button_id == 'refresh-button' and refresh_clicks:
        # Handle the "Refresh Data" button
        output_message = 'Data refreshed successfully!'
        return handle_refresh(refresh_clicks, fig1, fig2, output_message)

    elif button_id == 'prediction-button' and prediction_clicks:
        # Handle the "Show Prediction" button
        last_10_days, historical_data, prediction_figure, data_table = predict_price()

        # Display the predicted values and data table
        prediction_output = html.Div([
            html.H2('Historical Prices of the last 10 days and Predicted Prices for the next 30 days'),
            dcc.Graph(figure=prediction_figure),
            dash_table.DataTable(
                id='data-table',
                columns=[{'name': col, 'id': col} for col in data_table.columns],
                data=data_table.to_dict('records')
            )
        ])

        output_message = 'Data calculated and saved to Postgres Database'

        return [html.Div([
                    html.H2('Charts with historical data and streaming data from binance'),
                    dcc.Graph(figure=fig1),
                    dcc.Graph(figure=fig2),
                    prediction_output
                ]), output_message]

    else:
        return [html.Div([
                    html.H2('Charts with historical data and streaming data from binance'),
                    dcc.Graph(figure=fig1),
                    dcc.Graph(figure=fig2)
                ]), '']

def handle_refresh(refresh_clicks, fig1, fig2, output_message):
    # Handle the "Refresh Data" button
    return [html.Div([
                html.H2('Charts with historical data and streaming data from binance'),
                dcc.Graph(figure=fig1),
                dcc.Graph(figure=fig2)
            ]), output_message]

def handle_prediction(prediction_clicks, fig1, fig2, prediction_output, output_message):
    # Handle the "Show Prediction" button
    return [html.Div([
                html.H2('Charts with historical data and streaming data from binance'),
                dcc.Graph(figure=fig1),
                dcc.Graph(figure=fig2),
                prediction_output
            ]), output_message]

    
if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")