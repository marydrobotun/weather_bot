from bs4 import BeautifulSoup
import emoji
import requests
import json
import pprint
from config import weather_key
import pprint

def parse(coordinates):
    request = 'https://api.openweathermap.org/data/2.5/weather?lat=' \
              + str(coordinates['lat']) + '&lon=' + str(coordinates['lon']) + '&appid=' + weather_key + '&units=metric'
    weather = requests.get(request)
    pprint.pprint(json.loads(weather.text))
    json_weather = json.loads(weather.text)
    return json_weather



def get_coordinates(city):
    request ='http://api.openweathermap.org/geo/1.0/direct?q=' + city + '&limit=1&appid=' + weather_key
    result = requests.get(request)
    json_result = json.loads(result.text)
    if len(json_result) == 0:
        return False
    pprint.pprint(json_result)
    result = {}
    result['lat'] = json_result[0]['lat']
    result['lon'] = json_result[0]['lon']
    return result







if __name__=='__main__':
    get_coordinates('Москва')
    print(emoji.emojize('Python is :thumbs_up:'))