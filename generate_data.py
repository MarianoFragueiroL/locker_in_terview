import os
import random
import sys


from backend.utils.csv_file import CSVFile




def generate_data(amount_of_files, data_in_file=50):
    """
        This function creates a number of files indicated creating the csv with the fields indicated by the task
    """
    for index in range(int(amount_of_files)):
        fields = ['Marca', 'Tipo de producto', 'Valor calórico', '% de grasas saturadas', '% de azúcar', 'Establecimiento', 'Dirección', 'Horario de apertura', 'Horario de cierre','Precio']
        file_name = 'file_{}'.format(index)
        csv_file = CSVFile(file_name, fields)
        data = []
        for i in range(50):
            brand = f'Marca{i}'
            product_type = f'Tipo{i}'
            calories = random.randint(50, 500)
            saturated_fats_percentage = round(random.uniform(0, 30), 2)
            sugar_percentage = round(random.uniform(0, 30), 2)
            store = f'Establecimiento{i//10}'
            address = f'Dirección {i}'
            ## Makes sure the the open time is grater than the close time
            open_time = random.randint(0,16)
            close_time = random.randint(open_time,23)
            price = round(random.uniform(1, 10), 2)
            data.append([brand, product_type, calories, saturated_fats_percentage, sugar_percentage, store, address, open_time,close_time, price])
        csv_file.write_file(data)
    
    pass


if __name__ == "__main__":
    try:
        files = sys.argv[1]
        data = sys.argv[2]
        generate_data(files, data)
    except:
        files = sys.argv[1]
        generate_data(sys.argv[1])