import pandas as pd
from binance import Client
from config.data_yaml_generator import DataYamlGenerator
from sqlalchemy import create_engine
from DB.url_factory import UrlFactory
from sqlalchemy.engine import URL
from tools.decorators.logger import logger
from tools.decorators.timer import timer

class BinanceLoader:

    @logger    
    def __init__(self, destination_source, table_name, simbol, interval, start):
        
        dyg = DataYamlGenerator('config/secrets.yaml')
        binance_credentials = dyg.get_values(section='binance')        
        self.client = Client(binance_credentials['api_secret'], binance_credentials['api_secret'])
        self.destination_source = destination_source.name.lower()
        self.table_name = table_name
        self.simbol = simbol
        self.interval = interval
        self.start = start

    @logger
    def get_dataframe_lastday(self):

            data = self.client.get_historical_klines(self.simbol, self.interval, self.start)
            self.df_data = pd.DataFrame(data)


    @logger
    def format_df_columns(self):
            
            columns = {
                0: 'open_time',
                1: 'open_price',
                2: 'high_price',
                3: 'low_price',
                4: 'close_price',
                5: 'volume',
                6: 'close_time',
                7: 'quote_asset_volume',
                8: 'number_of_trades',
                9: 'taker_buy_base_asset_volume',
                10: 'taker_buy_quote_asset_volume',
                11: 'ignore'
            }

            self.df_data = self.df_data.rename(columns=columns)

    @logger
    def format_df_values(self):
        
        self.df_data.open_time = pd.to_datetime(self.df_data.open_time, unit='ms')
        self.df_data.close_time = pd.to_datetime(self.df_data.open_time, unit='ms')
        self.df_data.open_price = self.df_data.open_price.astype(float)
        self.df_data.high_price = self.df_data.high_price.astype(float)
        self.df_data.close_price = self.df_data.close_price.astype(float)

    @logger
    def exec_destination_source(self):
                
        if self.destination_source == 'csv':
            self.df_data.to_csv(f'data/{self.table_name}.csv', index=False)
        elif self.destination_source == 'json':
            self.df_data.to_json(f'data/{self.table_name}.json', orient='records', lines=True)
        if self.destination_source in ['sqlite', 'postgres', 'mysql']:
            uf = UrlFactory(self.destination_source)
            engine = create_engine(uf.get_url())
            self.df_data.to_sql(self.table_name, con=engine, index=False, if_exists='replace')

    @timer
    def generate(self):

        self.get_dataframe_lastday()
        self.format_df_columns()
        self.format_df_values()
        self.exec_destination_source()








