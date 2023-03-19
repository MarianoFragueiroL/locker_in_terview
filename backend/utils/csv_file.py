import csv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.

class CSVFile():
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    def __init__(self, file_name, fields = None) -> None:
        self.file_name = file_name
        self.fields = fields
    
    def read_file(self):
        route_file ='{}/csv_files/{}'.format(self.BASE_DIR, self.file_name)
        
        with open( route_file,  encoding="utf8", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            excel_data = [data for data in reader] 
        return excel_data

    def write_file(self, data):
        route_file ='{}/csv_files/{}.csv'.format(self.BASE_DIR, self.file_name)
        with open(route_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.fields)
            writer.writerows(data)
        pass