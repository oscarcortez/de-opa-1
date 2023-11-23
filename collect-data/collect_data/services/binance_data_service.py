# flake8: noqa
from ..repositories.binance_data_mysql_repository import BinanceDataMysqlRepository
from ..repositories.binance_data_postgres_repository import BinanceDataPostgresRepository
from ..repositories.binance_data_sqlite_repository import BinanceDataSqliteRepository
from ..repositories.binance_data_mongodb_repository import BinanceDataMongodbRepository
from ..repositories.binance_data_json_repository import BinanceDataJsonRepository
from ..repositories.binance_data_csv_repository import BinanceDataCsvRepository
from ..repositories.binance_data_repository import BinanceDataRepository


class BinanceDataService:
    def __init__(self, binace_data_repository: BinanceDataRepository) -> None:
        self.repository = binace_data_repository

    def load_from_dataframe(self, df_data, table_name):
        self.repository.set_table_name(table_name)
        self.repository.load_from_dataframe(df_data)

    def add_df(self, df_data):
        self.repository.add_df(df_new=df_data)

    def exists(self):
        return self.repository.exists()

    def find_all(self):
        return self.repository.find_all()
