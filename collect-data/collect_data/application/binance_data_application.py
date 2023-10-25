# flake8: noqa
from services.binance_data_service import BinanceDataService
from repositories.binance_data_mysql_repository import BinanceDataMysqlRepository
from repositories.binance_data_postgres_repository import BinanceDataPostgresRepository
from repositories.binance_data_sqlite_repository import BinanceDataSqliteRepository
from repositories.binance_data_mongodb_repository import BinanceDataMongodbRepository
from repositories.binance_data_json_repository import BinanceDataJsonRepository
from repositories.binance_data_csv_repository import BinanceDataCsvRepository
from repositories.binance_data_repository import BinanceDataRepository


class BinanceDataApplication:
    def __init__(self, destination_source=None, table_name=None):
        self.table_name = table_name
        self.destination_source = destination_source

    def str_to_class(self, class_name: str) -> BinanceDataRepository:
        result_class = globals()[class_name]
        return result_class()

    def set_binance_data_repository(self):
        binance_data_repository: BinanceDataRepository = self.str_to_class(
            self.destination_source
        )
        binance_data_repository.set_table_name(self.table_name)
        self.binance_data_service = BinanceDataService(binance_data_repository)

    def load_from_dataframe(self, df_binance):
        if self.binance_data_service.exists() == True:
        
            self.binance_data_service.add_df(
                df_data=df_binance
            )
        else:
            self.binance_data_service.load_from_dataframe(
                df_data=df_binance, table_name=self.table_name
            )
    
    def update_dataframe(self, df):
        pass

    def exists(self):
        return self.binance_data_service.exists()
