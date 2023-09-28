#from datetime import datetime
from tools.yaml_reader import YAMLReader
from tools.constants import Binance
from binance import Client
from tools.constants import Section
from api_client.binance_api_client import BinanceApiClient
from DB.sql_connections.postgres_connection import postgres_url_connection
from sqlalchemy import create_engine, inspect
import pandas as pd
import datetime

class BinanceDataUpdater:
    
    def __init__(self,
                 binance_client: Client,
                 secrets_settings: YAMLReader,
                 binance_api_client: BinanceApiClient,
                 binance_api_settings: YAMLReader,
                 ):
        self.secrets_settings = secrets_settings
        self.binance_client = binance_client
        self.binance_api_client = binance_api_client
        self.binance_api_settings = binance_api_settings

    def set_binance_client(self):

        credentials = self.secrets_settings.get_values(section = Section.BINANCE)
        self.binance_client.API_KEY = credentials['api_key']
        self.binance_client.API_SECRET = credentials['api_secret']
        

    def get_common_params(self):

        self.common_params = self.binance_api_settings.get_values(Binance.NAME)

    def get_type_data_params(self):
        self.type_data = 'binance_streaming_update'
        self.type_data_params = self.binance_api_settings.get_values(self.type_data)

    def build_binance_api_client(self):
        
        
        self.binance_api_client.client = self.binance_client
        self.binance_api_client.symbol = self.common_params['symbol']
        self.binance_api_client.interval = self.type_data_params['interval']
        self.binance_api_client.start = self.type_data_params['start']
        self.binance_api_client.end = self.type_data_params['end']

    def get_dataframe_from_api_client(self):
        
        self.dataframe = self.binance_api_client.get_dataframe()


    def append_to_dataframe(self):
        self.engine = create_engine(url= postgres_url_connection())
        self.table_name = 'streaming_data'
        self.dataframe.to_sql(
            self.table_name, 
            con= self.engine, 
            index=False, 
            if_exists='append'
        )
        self.engine.dispose()


    def show_in_terminal(self):
        print(datetime.datetime.now())
        print('Amount of currencies: ' + str(len(self.dataframe)))
        print('BTC Price of', self.dataframe['close_price'][0], "was inserted.")
        

    def execute_application(self):
        self.set_binance_client()
        self.get_common_params()
        self.get_type_data_params()
        self.build_binance_api_client()
        self.get_dataframe_from_api_client()
        self.append_to_dataframe()
        self.show_in_terminal()
        

    def execute(self):
        self.execute_application()





    