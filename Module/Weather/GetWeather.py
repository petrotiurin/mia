import json
from datetime import datetime
import requests
from SQLite.SQLite_CRUD_Querry import SQLite_Read


def weather(lat, lon):
    clear_data = dict()
    clear_data.update({'id': SQLite_Read.sqlite_count('weather') + 1})
    api = f'https://api.openweathermap.org/data/2.5/weather'
    token_weather = '&appid=4e77ac3694949ec2935fff1e3bb06a10'
    lang = '?lang=ru'
    gps = f"&lat={lat}&lon={lon}"
    metric = '&units=metric'
    response = requests.get(f'{api}{lang}{gps}{metric}{token_weather}')
    if response.status_code in [200]:
        txt = response.text
        # print(txt)
        txt = txt.replace(']', '')
        txt = txt.replace('[', '')
        txt = json.loads(txt)
        # print(txt)
        for key, values in txt.items():
            if isinstance(values, dict):
                for k2, v2 in values.items():
                    # print(f'{key}-{k2}-{v2}')
                    if (key in ['weather', 'main']) and \
                            (k2 in ['description', 'temp_min', 'temp_max', 'temp']):
                        if key == 'main':
                            clear_data.update({k2: v2})
                        else:
                            clear_data.update({key: v2})
                            clear_data.update({'write_datetime': datetime.now()})

            else:
                # print(f'{key}-{values}')
                if key in ['visibility', 'name']:
                    clear_data.update({key: values})
        return clear_data
