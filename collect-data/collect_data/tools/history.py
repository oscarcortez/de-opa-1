import csv

class History:

    def __init__(self):
        self.archivo_csv = 'data/history.csv'

    def add(self, table_name, datetime, rows):
        with open(self.archivo_csv, mode='a', newline='') as file:
            open_file = csv.writer(file)
            open_file.writerow([table_name, datetime, rows])