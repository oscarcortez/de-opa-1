from repositories.binance_data_repository import BinanceDataRepository
from DB.mongodb_connection import mongo_db, mongo_client
import pandas as pd


class BinanceDataMongodbRepository(BinanceDataRepository):
    def __init__(self, repository=None, table_name=None):
        self.repository = repository
        self.table_name = table_name
        self.collection = mongo_db[self.table_name]

    def set_table_name(self, table_name):
        self.table_name = table_name

    def load_from_dataframe(self, df_data: pd.DataFrame):
        documents = df_data.to_dict(orient="records")
        self.collection.drop()
        self.collection.insert_many(documents)

        mongo_client.close()

    def add_df(self, df_new: pd.DataFrame):
        documents = df_new.to_dict(orient="records")
        self.collection.insert_many(documents)
        mongo_client.close()

    def exists(self):
        result = self.table_name in mongo_db.list_collection_names()
        mongo_client.close()
        return result
