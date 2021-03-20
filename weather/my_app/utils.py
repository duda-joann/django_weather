import requests
from django.conf import settings
from .models import CityWeather, City


def get_weather():
    weather_data = []
    cities = City.objects.all()

    for city in cities:
        params = {
            'q': city,
            'units': 'metric',
            'appid': settings.API_KEY
        }
        data = requests.get(settings.API_URL, params=params)
        response = data.json()

        city_weather = {
            'city' : city.name,
            'temperature' : response['main']['temp'],
            'description' : response['weather'][0]['description'],
            'icon' : response['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    return weather_data


def save_to_database():
    weather_data = get_weather()

    for data in weather_data:
        CityWeather.save(**data)

