import requests
import gc

def get_data():
    response = requests.get('http://httpbin.org/json')
    if response.status_code == 200:
        return response.json()
    return -1

def garbageCollector(search_cls):
    searched_object = []    
    for obj in gc.get_objects():
        if isinstance(obj, search_cls):
            searched_object.append(obj)
    return searched_object
