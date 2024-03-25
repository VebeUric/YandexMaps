import sys
from io import BytesIO
import tempfile

import requests

class Geocoder:
    def __init__(self, toponym_to_find=None):
        self.geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
        self.api_key = "40d1649f-0493-4b70-98ba-98533de7710b"
        self.toponym_to_find = toponym_to_find
        self.geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": self.toponym_to_find,
            "format": "json"}


    def do_request(self):
        response = requests.get(self.geocoder_api_server, params=self.geocoder_params)
        if response:
           self.response = response.json()
           return self.response

    def set_adress(self, adress):
        self.geocoder_params['geocode'] = adress

class StaticAPI:
    def __init__(self, lon=None, lat=None, spn=1):
        self.map_api_server = "http://static-maps.yandex.ru/1.x/"
        self.spn = spn
        self.point = []
        self.lon = lon
        self.lat = lat
        self.map_params = {'ll':','.join([str(lon), str(lat)]), "l": "map", 'spn': f'{spn},{spn}', 'size': f'{650},{450}'}


    def set_mode(self, mode):
        self.map_params['l'] = mode
    def set_spn(self, spn):
        self.map_params['spn'] = f'{spn},{spn}'
    def set_coords(self, lon, lat):
       self.map_params['ll'] = f'{lon},{lat}'

    # def set_point(self, coord_x, coord_y):
    #     self.params['pt'] = ','.join(coord_x, coord_y)

    def get_static_image(self):
         print(self.map_params)
         image = requests.get(self.map_api_server, params=self.map_params)

         with tempfile.NamedTemporaryFile(delete=False) as f:
             f.write(image.content)
             return f.name