import requests
from pprint import pprint
def send_api_request(city,state,country,key):
    string_builder = f'{city},{state},{country}'

    query = {'q':string_builder, 'units':'Imperial', 'appid': key}

    url = 'http://api.openweathermap.org/data/2.5/forecast'

    data = requests.get(url, params=query).json()

    return data
