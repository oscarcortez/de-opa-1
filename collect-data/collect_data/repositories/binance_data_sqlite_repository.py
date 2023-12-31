from repositories.binance_data_repository import BinanceDataRepository
from DB.sql_connections.sqlite_connection import sqlite_url_connection
from sqlalchemy import create_engine, inspect
import pandas as pd

class BinanceDataSqliteRepository(BinanceDataRepository):
    
    def __init__(self, table_name = None):

        self.engine = create_engine(url= sqlite_url_connection())
        self.table_name = table_name

    def set_table_name(self, table_name):

        self.table_name = table_name

    def load_from_dataframe(self, df_data: pd.DataFrame):                

        df_data.to_sql(
            self.table_name, 
            con= self.engine, 
            index=False, 
            if_exists='replace'
        )

        self.engine.dispose()
    
    def add_df(self, df_new: pd.DataFrame):
        
        df_new.to_sql(
            self.table_name, 
            self.engine, 
            if_exists='append', 
            index=False
            )

        self.engine.dispose()
    
    def exists(self):

        result = self.table_name in inspect(self.engine).get_table_names()
        self.engine.dispose()
        return result