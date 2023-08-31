from tools.constants import Constants as C, RelativePath, File
#from binance_data_repository import BinanceDataRepository
from tools.env_selector import EnvSelector
from config.data_yaml_generator import DataYamlGenerator


class BinanceDataJsonRepository:

    def __init__(self, repository = File.JSON):
        
        self.repository= repository
        self.dyg = DataYamlGenerator(yaml_file= RelativePath.ENV_SETTINGS)

    def load_from_dataframe(self, df_data, table_name = None):

        path = self.dyg.get_values(section= self.repository)['path']
        df_data.to_json(
            f'{path}{table_name}.{File.JSON}', 
            orient='records', lines=True
        )
