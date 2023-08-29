import csv
from tools.constants import Constants as C
class History:

    def __init__(self):
        self.archivo_csv = C.PATH_HISTORY_CSV

    def add(self, table_name, datetime, rows):
        with open(self.archivo_csv, mode='a', newline='') as file:
            open_file = csv.writer(file)
            open_file.writerow([table_name, datetime, rows])