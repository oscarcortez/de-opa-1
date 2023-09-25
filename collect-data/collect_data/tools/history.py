import csv
from tools.constants import RelativePath
from tools.yaml_reader import YAMLReader


class History:
    def __init__(self, path_settings: str = RelativePath.ENV_SETTINGS):
        dyg = YAMLReader(yaml_file=path_settings)
        self.history_path = dyg.get_values(section="history")["path"]

    def add(self, table_name, datetime, rows,
            environment, destination_source, symbol):
        with open(self.history_path, mode="a", newline="") as file:
            open_file = csv.writer(file)
            open_file.writerow([
                    table_name,
                    datetime,
                    rows,
                    environment,
                    destination_source,
                    symbol
            ])
