import requests
import gc

def get_data():
    response = requests.get('http://httpbin.org/json')
    if response.status_code == 200:
        return response.json()
    return -1
