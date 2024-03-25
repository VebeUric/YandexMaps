import sys
import requests
from PIL import Image
from io import BytesIO
from web_func import make_appropriate_scale

toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
map_api_server = "http://static-maps.yandex.ru/1.x/"
api_key = "40d1649f-0493-4b70-98ba-98533de7710b"

geocoder_params = {
    "apikey": api_key,
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)
result_tmp_response = response.json()
size = make_appropriate_scale(result_tmp_response)

if not response:
    pass

json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]
toponym_coodrinates = toponym["Point"]["pos"]
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

map_params = {"ll": ",".join([toponym_longitude, toponym_lattitude]), "l": "map", 'spn': f'{size}',
              'pt': ','.join(toponym_coodrinates.split())}

response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()
