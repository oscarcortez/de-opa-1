from services.binance_data_service import BinanceDataService
from tools.str_short_to_complete import str_short_to_complete as str_complete

from repositories.binance_data_mysql_repository import BinanceDataMysqlRepository
from repositories.binance_data_postgres_repository import BinanceDataPostgresRepository
from repositories.binance_data_sqlite_repository import BinanceDataSqliteRepository
from repositories.binance_data_mongodb_repository import BinanceDataMongodbRepository
from repositories.binance_data_json_repository import BinanceDataJsonRepository
from repositories.binance_data_csv_repository import BinanceDataCsvRepository

class BinanceDataApplication:
 
    def __init__(self, destination_source= None, table_name= None):
            
        self.table_name = table_name
        self.destination_source = destination_source        

    def set_binance_data_repository(self):

        self.destination_source = str_complete(self.destination_source)
        binance_data_repository = globals()[self.destination_source]
        binance_data_repository = binance_data_repository()
        self.binance_data_service = BinanceDataService(binance_data_repository)

    def load_from_dataframe(self, df_binance):
        self.binance_data_service.load_from_dataframe(df_data= df_binance, table_name= self.table_name)
        


