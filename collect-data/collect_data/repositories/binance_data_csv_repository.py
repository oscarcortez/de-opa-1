from repositories.binance_data_repository import BinanceDataRepository
from tools.constants import File, RelativePath
from tools.yaml_reader import YAMLReader
import pandas as pd
import os

class BinanceDataCsvRepository(BinanceDataRepository):

    def __init__(self, repository = File.CSV, table_name = None):
        
        self.repository= repository
        dyg = YAMLReader(yaml_file= RelativePath.ENV_SETTINGS)
        self.table_name = table_name
        self.path = dyg.get_values(section= self.repository)['path']

    def set_table_name(self, table_name):

        self.table_name = table_name

    def load_from_dataframe(self, df_data: pd.DataFrame):
                
        df_data.to_csv(
            f'{self.path}{self.table_name}.{File.CSV}', 
            index=False
        )

    def add_df(self, df_new: pd.DataFrame):
                
        current_csv_file = f'{self.path}{self.table_name}.{File.CSV}'
        df_current = pd.read_csv(current_csv_file)
        df_result = pd.concat([df_current, df_new], ignore_index=True)
        df_result.to_csv(current_csv_file, index=False)

    def exists(self):

        return os.path.isfile(f'{self.path}{self.table_name}.{File.CSV}')
