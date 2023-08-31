import csv
from tools.constants import RelativePath
from tools.data_yaml_generator import DataYamlGenerator

class History:

    def __init__(self):
        dyg = DataYamlGenerator(yaml_file= RelativePath.ENV_SETTINGS)          
        self.file_path = dyg.get_values(section= 'history')['path']

    def add(self, table_name, datetime, rows, environment, destination_source, symbol):
        with open(self.file_path, mode='a', newline='') as file:
            open_file = csv.writer(file)
            open_file.writerow([table_name, datetime, rows, environment, destination_source, symbol])
