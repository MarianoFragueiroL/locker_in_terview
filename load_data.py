import requests
import os
import json

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
            create_product_url = main_url + "product"
            data_product_to_create = {
                "branch": row['Marca'],
                "product_type": row['Tipo de producto'],
                "calories": int(row['Valor calórico']),
                "saturated_fats_percentage": float(row['% de grasas saturadas']),
                "sugar_percentage": float(row['% de azúcar'])
            }
            product_response = requests.post(url=create_product_url, json=data_product_to_create)
            if product_response.status_code == 500:
                continue
            product_id =json.loads(product_response.text)['id']
 
            create_store_url = main_url + "store"
            data_store_to_create = {
                "name": row['Establecimiento'],
                "address": row['Dirección'],
                "open_time": row['Horario de apertura'],
                "close_time": row['Horario de cierre']
            }
            store_response = requests.post(create_store_url, json=data_store_to_create)
            store_id =json.loads(store_response.text)['id']
            if store_response.status_code == 500:
                continue
            set_price_url = main_url + "price"
            data_to_set_price = {
                "store": {
                        "id": int(store_id)
                    },
                "product": {
                    "id": int(product_id)
                    },
                "price": float(row['Precio'])
            }
            requests.post(set_price_url, json=data_to_set_price)
            
        break



if __name__ == '__main__':
    main()