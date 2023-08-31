from DB.mongodb_connection import mongo_db

class BinanceDataMongodbRepository:

    def __init__(self, repository = None):
        
        self.repository= repository

    def load_from_dataframe(self, df_data, table_name = None):

        collection = mongo_db[table_name]
        documents = df_data.to_dict(orient='records')
        collection.drop()
        collection.insert_many(documents)