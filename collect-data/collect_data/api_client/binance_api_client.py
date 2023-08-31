from tools.env_selector import EnvSelector
from config.data_yaml_generator import DataYamlGenerator
from binance import Client
import pandas as pd
from tools.constants import Constants as C
from tools.constants import RelativePath
from tools.constants import Section

class BinanceApiClient:

    def __init__(self, symbol= None, interval= None, start= None, end = None):

        secrets = DataYamlGenerator(yaml_file= RelativePath.SECRETS)
        binance_credentials = secrets.get_values(section = Section.BINANCE)
        self.client = Client(binance_credentials['api_key'], binance_credentials['api_secret'])
    
        self.symbol = symbol
        self.interval = interval
        self.start = start
        self.end = end
    
    def set_start(self, start):
        self.start = start

    def set_end(self, end):
        self.end = end
        
    def resources_to_dataframe(self):

        data = self.client.get_historical_klines(self.symbol, self.interval, self.start, self.end)
        self.df_data = pd.DataFrame(data)
        self.df_shape = self.df_data.shape
    
    def rename_df_columns(self):
        
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
    
        
    def format_df_values(self):
        
        self.df_data.open_time = pd.to_datetime(self.df_data.open_time, unit='ms')
        self.df_data.close_time = pd.to_datetime(self.df_data.close_time, unit='ms')
        self.df_data.open_price = self.df_data.open_price.astype(float)
        self.df_data.high_price = self.df_data.high_price.astype(float)
        self.df_data.close_price = self.df_data.close_price.astype(float)
    
    def get_dataframe(self):

        self.resources_to_dataframe()
        self.rename_df_columns()
        self.format_df_values()

        return self.df_data