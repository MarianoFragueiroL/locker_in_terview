import requests
import os

from pathlib import Path
from backend.utils.csv_file import CSVFile


def main():
    """
        This function read the files on the folder /csv_files/
        Get all the data and send toe the API of Django to create the products
    """
    main_url = 'http://127.0.0.1:8000/'
    BASE_DIR = Path(__file__).resolve().parent
    folder_path = '{}/csv_files/'.format(BASE_DIR) 
    file_names = os.listdir(folder_path)
    for file_name in file_names:
        csv_file = CSVFile(file_name)
        csv_data = csv_file.read_file()
        for row in csv_data:
            create_product_url = main_url + "product/"
            data_product_to_create = {
                "branch": row['Marca'],
                "product_type": row['Tipo de producto'],
                "calories": int(row['Valor calórico']),
                "saturated_fats_percentage": float(row['% de grasas saturadas']),
                "sugar_percentage": float(row['% de azúcar'])
            }
            response = requests.post(url=create_product_url, json=data_product_to_create)
            if response.status_code == 500:
                continue
            create_store_url = main_url + "store/"
            data_store_to_create = {
                "name": row['Establecimiento'],
                "address": row['Dirección'],
                "schedule": row['Horario']
            }
            response = requests.post(create_store_url, json=data_store_to_create)

            if response.status_code == 500:
                continue
            set_price_url = main_url + "price/"
            data_to_set_price = {
                "store": {
                        "name": row['Establecimiento'],
                        "address": row['Dirección']
                    },
                "product": {
                    "branch": row['Marca'],
                    "product_type": row['Tipo de producto'],
                    },
                "price": float(row['Precio'])
            }
            requests.post(set_price_url, json=data_to_set_price)




if __name__ == '__main__':
    main()