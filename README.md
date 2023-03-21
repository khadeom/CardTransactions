# CardTransactions

## Steps to follow to run this project
  - pip install requirements.txt
  - python manage.py runserver
  
Use post man to upload the Short electronic-card-transactions-february-2023-csv-tables - electronic-card-transactions-february-2023-csv-tables.csv.csv 
at http://127.0.0.1:8000/addcsv/

To sort run get request at http://127.0.0.1:8000/sort/?column_name=data_value&sort_order=asc
 
I have also added postman collection `Transactions.postman_collection.json` to test the api.
