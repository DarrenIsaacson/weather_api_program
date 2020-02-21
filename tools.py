from datetime import datetime

def seperate_needed_data(data):
    string_store = []

    for days in data['list']:
        date_converted = datetime.fromtimestamp(int(days['dt'])).strftime('%d-%m-%Y %I:%M:%p')
        high_temp = days['main']['temp_max']
        low_temp = days['main']['temp_min']
        wind_speed = days['wind']['speed']


        string_store.append(f'{date_converted}\n***************\nHigh Temp: {high_temp} \nLow Temp: {low_temp} \nWind Speed: {wind_speed}\n')


    return string_store
