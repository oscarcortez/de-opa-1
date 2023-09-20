from repositories.binance_data_repository import BinanceDataRepository
from tools.constants import RelativePath, File
from tools.yaml_reader import YAMLReader
import pandas as pd
import os


class BinanceDataJsonRepository(BinanceDataRepository):
    def __init__(self, repository=File.JSON, table_name=None):
        self.repository = repository
        dyg = YAMLReader(yaml_file=RelativePath.ENV_SETTINGS)
        self.table_name = table_name
        self.path = dyg.get_values(section=self.repository)["path"]

    def set_table_name(self, table_name):
        self.table_name = table_name

    def load_from_dataframe(self, df_data: pd.DataFrame):
        df_data.to_json(
            f"{self.path}{self.table_name}.{File.JSON}",
            orient="records",
            lines=True
        )

    def add_df(self, df_new):
        current_json_file = f"{self.path}{self.table_name}.{File.JSON}"
        df_current = pd.read_json(current_json_file)
        df_result = pd.concat([df_current, df_new], ignore_index=True)
        df_result.to_json(current_json_file, index=False)

    def exists(self):
        print("table_name:", self.table_name)
        print(
            f"{self.path}{self.table_name}.{File.JSON}:",
            os.path.isfile(f"{self.path}{self.table_name}.{File.JSON}"),
        )
        return os.path.isfile(f"{self.path}{self.table_name}.{File.JSON}")
