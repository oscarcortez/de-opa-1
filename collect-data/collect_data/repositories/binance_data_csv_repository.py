from tools.constants import File, RelativePath
from tools.yaml_reader import YAMLReader

class BinanceDataCsvRepository:

    def __init__(self, repository = File.CSV):
        
        self.repository= repository
        self.dyg = YAMLReader(yaml_file= RelativePath.ENV_SETTINGS)

    def load_from_dataframe(self, df_data, table_name = None):
        
        path = self.dyg.get_values(section= self.repository)['path']
        df_data.to_csv(f'{path}{table_name}.{File.CSV}', index=False)
