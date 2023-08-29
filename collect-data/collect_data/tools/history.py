import csv
from tools.constants import Constants as C
from tools.env_selector import EnvSelector
class History:

    def __init__(self):        
        env = EnvSelector()
        self.file_path = env.get_history_path()

    def add(self, table_name, datetime, rows):
        with open(self.file_path, mode='a', newline='') as file:
            open_file = csv.writer(file)
            open_file.writerow([table_name, datetime, rows])