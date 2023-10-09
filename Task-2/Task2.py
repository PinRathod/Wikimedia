import requests
import csv

with open ('Task 2 - Intern.csv',newline='',encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    next(reader)
    for url in reader:
        try:
            fetch_url=url[0]
            response = requests.get(fetch_url) 

            status_code = response.status_code
            print(f"({status_code}) {fetch_url}")

        except Exception as e:
            print(f"(Connection Error) {fetch_url}")
        


