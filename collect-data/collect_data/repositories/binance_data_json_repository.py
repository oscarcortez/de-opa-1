from tools.constants import RelativePath, File
from tools.yaml_reader import YAMLReader

class BinanceDataJsonRepository:

    def __init__(self, repository = File.JSON):
        
        self.repository= repository
        self.dyg = YAMLReader(yaml_file= RelativePath.ENV_SETTINGS)

    def load_from_dataframe(self, df_data, table_name = None):

        path = self.dyg.get_values(section= self.repository)['path']
        df_data.to_json(
            f'{path}{table_name}.{File.JSON}', 
            orient='records', lines=True
        )
