import pandas as pd
from binance import Client
from config.data_yaml_generator import DataYamlGenerator
from tools.decorators.logger import logger
from tools.decorators.timer import timer
from tools.decorators.show_properties import show_properties
from tools.constants import Constants as C
from tools.history import History
from datetime import datetime
from tools.env_selector import EnvSelector
from services.binance_data_service import BinanceDataService
from tools.str_short_to_complete import str_short_to_complete as str_complete

from repositories.binance_data_mysql_repository import BinanceDataMysqlRepository
from repositories.binance_data_postgres_repository import BinanceDataPostgresRepository
from repositories.binance_data_sqlite_repository import BinanceDataSqliteRepository
from repositories.binance_data_mongodb_repository import BinanceDataMongodbRepository
from repositories.binance_data_json_repository import BinanceDataJsonRepository
from repositories.binance_data_csv_repository import BinanceDataCsvRepository



#@show_properties
class BinanceDataApplication:

    #@logger    
    def __init__(self, destination_source= None, table_name= None):
            
        self.table_name = table_name
        # self.history = History()
        #self.set_binance_data_repository(destination_source= destination_source)
        self.destination_source = destination_source        

    def set_binance_data_repository(self):

        self.destination_source = str_complete(self.destination_source)
        binance_data_repository = globals()[self.destination_source]
        binance_data_repository = binance_data_repository()
        self.binance_data_service = BinanceDataService(binance_data_repository)

    #@logger
    def load_from_dataframe(self, df_binance):
        self.binance_data_service.load_from_dataframe(df_data= df_binance, table_name= self.table_name)
        
    # def print_df_columns_rows(self):
    #     print(f'From Binance API were loaded: {self.df_shape[0]} rows and {self.df_shape[1]} columns')

    # @logger
    # def save_history(self):
    #     self.history.add(self.table_name, datetime= datetime.now().strftime("%Y-%m-%d %H:%M:%S"), rows= self.df_shape[0] )







