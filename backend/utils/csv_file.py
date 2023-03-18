import csv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.

class CSVFile():
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    def __init__(self, file_name, fields) -> None:
        self.file_name = file_name
        self.fields = fields
    
    def read_file(self):

        with open( self.file_name+'.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)


    def write_file(self, data):
        base_dir = self.BASE_DIR
        route_file ='{}/csv_files/{}.csv'.format(base_dir, self.file_name)
        with open(route_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.fields)
            writer.writerows(data)
        pass