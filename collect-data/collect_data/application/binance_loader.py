import pandas as pd
from binance import Client
from config.data_yaml_generator import DataYamlGenerator
from sqlalchemy import create_engine
from DB.url_factory import UrlFactory
import time

class BinanceLoader:
    
    def __init__(self, destination_source, table_name, simbol, interval, start):
        
        print('Initiating Binance Loader...')
        try: 
            dyg = DataYamlGenerator('config/secrets.yaml', 'binance')
            binance_credentials = dyg.get_values({'api_key','api_secret'})        
            self.client = Client(binance_credentials['api_secret'], binance_credentials['api_secret'])
            self.destination_source = destination_source.name.lower()
            self.table_name = table_name
            self.simbol = simbol
            self.interval = interval
            self.start = start

        except Exception as e: 
            print("init: Error ocurred: ", e)
        else:
            print("init: pass")

    def get_dataframe_lastday(self):

        try:
            data = self.client.get_historical_klines(self.simbol, self.interval, self.start)
            self.df_data = pd.DataFrame(data)

        except Exception as e: 
            print("get dataframe lastday: Error ocurred: ", e)
        else:
            print("get dataframe lastday: pass")


    def format_df_columns(self):
        try: 
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
        
        except Exception as e: 
            print("format df columns: Error ocurred: ", e)
        else:
            print("format df columns: pass")

    def format_df_values(self):
        
        try: 
            self.df_data.open_time = pd.to_datetime(self.df_data.open_time, unit='ms')
            self.df_data.close_time = pd.to_datetime(self.df_data.open_time, unit='ms')
            self.df_data.open_price = self.df_data.open_price.astype(float)
            self.df_data.high_price = self.df_data.high_price.astype(float)
            self.df_data.close_price = self.df_data.close_price.astype(float)

        except Exception as e: 
            print("format_df_values: Error ocurred: ", e)
        else:
            print("format_df_values: pass")

    def exec_destination_source(self):
        try:             
            if self.destination_source == 'csv':
                self.df_data.to_csv(f'{self.table_name}.csv', index=False)
            elif self.destination_source == 'json':
                self.df_data.to_json(f'{self.table_name}.json', orient='records', lines=True)
            if self.destination_source == ['mysql','postgres','sqlite']:
                uf = UrlFactory(self.destination_source)
                engine = create_engine(uf.get_url())
                self.df_data.to_sql(self.table_name, con=engine, index=False, if_exists='replace')
        
        except Exception as e: 
            print("destination_source: Error ocurred: ", e)
        else:
            print("destination_source: pass")

    def generate(self):

        start_time = time.time()

        self.get_dataframe_lastday()
        self.format_df_columns()
        self.format_df_values()
        self.exec_destination_source()

        end_time = time.time()

        execution_time = end_time - start_time

        print(f'generate: pass in {execution_time:.2f} seconds')






