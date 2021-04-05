import requests
from django.conf import settings
from .models import CityWeather, City


def get_api(city):
    params = {
        'q': city,
        'units': 'metric',
        'appid': settings.API_KEY
    }
    data = requests.get(settings.API_URL, params=params)
    if data.status_code == 200:
        response = data.json()
        return response
    else:
        return None


def get_weather():
    weather_data = []
    cities = City.objects.all()

    for city in cities:
        response = get_api(city)
        if response:
            city_weather = {
                    'city': city.name,
                    'temperature': response['main']['temp'],
                    'description': response['weather'][0]['description'],
                    'icon': response['weather'][0]['icon'],
                }

            weather_data.append(city_weather)

    return weather_data


def save_to_database():
    weather_data = get_weather()

    for data in weather_data:
        CityWeather.save(**data)

