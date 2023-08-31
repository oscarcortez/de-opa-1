
# from sqlalchemy import create_engine
# from DB.url_factory import UrlFactory

# class BinanceDataSqlRepository:

#     def __init__(self, repository = None):
        
#         self.repository= repository

#     def load_from_dataframe(self, df_data, table_name = None):

#         uf = UrlFactory(self.repository)
#         engine = create_engine(uf.get_url())
#         df_data.to_sql(table_name, con=engine, index=False, if_exists='replace')

