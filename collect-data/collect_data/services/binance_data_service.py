from repositories.binance_data_mysql_repository import BinanceDataMysqlRepository
from repositories.binance_data_postgres_repository import BinanceDataPostgresRepository
from repositories.binance_data_sqlite_repository import BinanceDataSqliteRepository
from repositories.binance_data_mongodb_repository import BinanceDataMongodbRepository
from repositories.binance_data_json_repository import BinanceDataJsonRepository
from repositories.binance_data_csv_repository import BinanceDataCsvRepository


class BinanceDataService:

    def __init__(self, binace_data_repository) -> None:
        self._repository = binace_data_repository
        

    def load_from_dataframe(self, df_data, table_name):
        self._repository.load_from_dataframe(df_data, table_name)
