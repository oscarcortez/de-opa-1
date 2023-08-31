from DB.sql_connections.postgres_connection import postgres_url_connection
from sqlalchemy import create_engine

class BinanceDataPostgresRepository:
    
    def __init__(self):
        pass

    def load_from_dataframe(self, df_data, table_name):

        engine = create_engine(url= postgres_url_connection())        
        df_data.to_sql(table_name, con=engine, index=False, if_exists='replace')