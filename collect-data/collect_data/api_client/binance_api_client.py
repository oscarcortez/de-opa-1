from binance import Client
import pandas as pd
from tools.constants import DF


class BinanceApiClient:
    def __init__(
        self, client: Client = None, symbol=None, interval=None, start=None, end=None
    ):
        self.client = client
        self.symbol = symbol
        self.interval = interval
        self.start = start
        self.end = end

    def set_client(self, client: Client):
        self.client = client

    def set_start(self, start):
        self.start = start

    def set_end(self, end):
        self.end = end

    def data_to_dataframe(self):
        if self.end is None:
            data = self.client.get_historical_klines(
                self.symbol, self.interval, self.start
            )
        else:
            data = self.client.get_historical_klines(
                self.symbol, self.interval, self.start, self.end
            )
        self.df_data = pd.DataFrame(data)
        self.df_shape = self.df_data.shape

    def rename_df_columns(self):
        columns = {
            0: DF.COL_0,
            1: DF.COL_1,
            2: DF.COL_2,
            3: DF.COL_3,
            4: DF.COL_4,
            5: DF.COL_5,
            6: DF.COL_6,
            7: DF.COL_7,
            8: DF.COL_8,
            9: DF.COL_9,
            10: DF.COL_10,
            11: DF.COL_11,
        }

        self.df_data = self.df_data.rename(columns=columns)

    def format_df_values(self):
        self.df_data.open_time = pd.to_datetime(self.df_data.open_time, unit="ms")
        self.df_data.close_time = pd.to_datetime(self.df_data.close_time, unit="ms")
        self.df_data.open_price = self.df_data.open_price.astype(float)
        self.df_data.high_price = self.df_data.high_price.astype(float)
        self.df_data.close_price = self.df_data.close_price.astype(float)

    def get_dataframe(self):
        self.data_to_dataframe()
        if self.df_data.shape[0] > 0:
            self.rename_df_columns()
            self.format_df_values()

        return self.df_data
    
    def last_data_to_dataframe(self):
        self.get_dataframe()
        return self.df_data.iloc[[-1]]
