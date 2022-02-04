import requests
import csv
from src.uczen import Uczen
from src.przedmiot import Przedmiot

def get_data():
    response = requests.get('http://httpbin.org/json')
    if response.status_code == 200:
        return response.json()
    return -1

# def parse_uczen_data_from_csv(file):
#     with open(f"{file}", 'r') as uczen_csv:
#         csv_reader = csv.reader(uczen_csv, delimiter=';')
#         for line in csv_reader:
#             Uczen.create_uczen(line[0], line[1], line[2], line[3])
#     return
#
# def parse_przedmiot_data_from_csv(file):
#     with open(f"{file}", 'r') as przedmiot_csv:
#         csv_reader = csv.reader(przedmiot_csv, delimiter=';')
#         for line in csv_reader:
#             Przedmiot.create_przedmiot(line[0], line[1])
#     return
