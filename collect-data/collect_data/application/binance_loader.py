import pandas as pd
from binance import Client
from config.data_yaml_generator import DataYamlGenerator
from sqlalchemy import create_engine
from DB.url_factory import UrlFactory
from sqlalchemy.engine import URL
from tools.decorators.logger import logger
from tools.decorators.timer import timer
from tools.decorators.show_properties import show_properties
from tools.constants import Constants as C
from tools.history import History
from datetime import datetime
from DB.mongodb_connection import mongo_db
@show_properties
class BinanceLoader:

    @logger    
    def __init__(self, destination_source, table_name, symbol, interval, start, end = None):
        
        self.dyg = DataYamlGenerator(C.PATH_CONFIG_SECRETS_YAML)
        binance_credentials = self.dyg.get_values(section= C.YAML_SECTION_BINANCE)
        self.client = Client(binance_credentials['api_key'], binance_credentials['api_secret'])
        self.destination_source = destination_source
        self.table_name = table_name
        self.symbol = symbol
        self.interval = interval
        self.start = start
        self.end = end
        self.history = History()

    @logger
    def get_dataframe(self):

        data = self.client.get_historical_klines(self.symbol, self.interval, self.start, self.end)
        self.df_data = pd.DataFrame(data)
        self.df_shape = self.df_data.shape


    @logger
    def format_df_columns(self):
            
            columns = {
                0:  C.DF_COL_0,
                1:  C.DF_COL_1,
                2:  C.DF_COL_2,
                3:  C.DF_COL_3,
                4:  C.DF_COL_4,
                5:  C.DF_COL_5,
                6:  C.DF_COL_6,
                7:  C.DF_COL_7,
                8:  C.DF_COL_8,
                9:  C.DF_COL_9,
                10: C.DF_COL_10,
                11: C.DF_COL_11
            }

            self.df_data = self.df_data.rename(columns=columns)

    @logger
    def format_df_values(self):
        
        self.df_data.open_time = pd.to_datetime(self.df_data.open_time, unit='ms')
        self.df_data.close_time = pd.to_datetime(self.df_data.close_time, unit='ms')
        self.df_data.open_price = self.df_data.open_price.astype(float)
        self.df_data.high_price = self.df_data.high_price.astype(float)
        self.df_data.close_price = self.df_data.close_price.astype(float)

    @logger
    def exec_destination_source(self):

        self.dyg.set_yaml_file(C.PATH_CONFIG_SETTINGS_YAML)    
        if self.destination_source == C.CSV:
            path = self.dyg.get_values(section= C.CSV)['path']
            self.df_data.to_csv(f'{path}{self.table_name}.{C.CSV}', index=False)
        elif self.destination_source == C.JSON:
            path = self.dyg.get_values(section= C.JSON)['path']
            self.df_data.to_json(f'{path}{self.table_name}.{C.JSON}', orient='records', lines=True)
        elif self.destination_source in [C.DB_MYSQL, C.DB_POSTGRES, C.DB_SQLITE]:
            uf = UrlFactory(self.destination_source)
            engine = create_engine(uf.get_url())
            self.df_data.to_sql(self.table_name, con=engine, index=False, if_exists='replace')
        elif self.destination_source == C.DB_MONGODB:            
            collection = mongo_db[self.table_name]
            documents = self.df_data.to_dict(orient='records')
            collection.drop()
            collection.insert_many(documents)

    def print_df_columns_rows(self):
        print(f'From Binance API were loaded: {self.df_shape[0]} rows and {self.df_shape[1]} columns')

    @logger
    def save_history(self):
        self.history.add(self.table_name, datetime= datetime.now().strftime("%Y-%m-%d %H:%M:%S"), rows= self.df_shape[0] )
    
    @timer
    def generate(self):

        self.get_dataframe()
        self.format_df_columns()
        self.format_df_values()
        self.exec_destination_source()
        self.print_df_columns_rows()
        self.save_history()






