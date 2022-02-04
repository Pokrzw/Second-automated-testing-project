import requests
import csv
from src.uczen import Uczen
from src.przedmiot import Przedmiot

def get_data():
    response = requests.get('http://httpbin.org/json')
    if response.status_code == 200:
        return response.json()
    return -1
