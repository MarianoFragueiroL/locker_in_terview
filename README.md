Part 1
    - Create sctipt generate_data.py that generates an initial data set in a cvs file (the amount of file that you want)


Part 2
    - Create a DB (SQLite)  

Part 3
    - Create an API REST that allows:
        - Add product
        - Modify product
        - Add store
        - Assign price of product in a store
        - Get all products of one store


Part 4
    - Create script that load in the DB all the data generated in the "part 1", using the API of the "part 3"




In order to execute the API and 
Install dependencies:

pip install -r requirements.txt

1) Generate data:
    To execute the file generate_data.py execute the following command:
        To generate 50 rows of data:
            python generate_data.py <amount of csv files that I want to generate>
            In case that you have more than one python version
            python3 generate_data.py <amount of csv files that I want to generate> 
        To indicate the amount of rows of data:
            python generate_data.py <amount of csv files that I want to generate> <amount of data to generate>


2) Generate database:
    python manage.py migrate
    Or python3 manage.py migrate


3) API REST:
    In local case baseurl =  http://127.0.0.1:8000/
        - Add product:
            <baseurl>product/
            data to send:
            {
                "branch": "some2",
                "product_type": "cookie",
                "calories": 500,
                "saturated_fats_percentage": 8,
                "sugar_percentage": 10
            }

        - Modify product
            <baseurl>product/<branch_name>
            data to send to modify calories for example:
            {
                "branch": "some",
                "product_type": "apple",
                "calories": 400,
            }
        - Add store
            <baseurl>store/
            data to send :
            {
                "name": "AppleStore",
                "address": "Carrer de Gran Via 456",
                "schedule": "8:00 - 16:00"
            }
        - Assign price of product in a store
            <baseurl>price/
            data to send:
            {
            "store": {
                    "name": "AppleStore"
                },
            "product": {
                    "product_type": "cookie",
                    "branch": "some2"
                },
            "price": 40
            }
        - Get all the products of one store