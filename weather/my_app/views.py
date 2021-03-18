from django import http
from django.views.decorators.cache import cache_page
import requests
from django.shortcuts import render, redirect
from django.conf import settings
from .models import City
from .forms import CityForm

@cache_page(60  * 15)
def index(request : http.request) -> http.response:
    """
    render main page with weather
    """
    url = 'http://api.openweathermap.org/data/2.5/weather'

    err_msg = ''
    message = ''
    message_class = ''

    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()
            
            if existing_city_count == 0:
                params = {
                    'q': new_city,
                    'units': 'metric',
                    'appid': settings.API_KEY
                }
                response = requests.get(url, params=params)

                if response.status_code == 200:
                    form.save()
                else:
                    err_msg = 'City does not exist in the world!'
            else:
                err_msg = 'City already exists in the database!'

        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City added successfully!'
            message_class = 'is-success'

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        params = {
            'q': city,
            'units': 'metric',
            'appid': settings.API_KEY
        }
        data = requests.get(url, params=params)
        response = data.json()

        city_weather = {
            'city' : city.name,
            'temperature' : response['main']['temp'],
            'description' : response['weather'][0]['description'],
            'icon' : response['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {
        'weather_data' : weather_data, 
        'form' : form,
        'message' : message,
        'message_class' : message_class
    }

    return render(request, 'weather.html', context)


def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()
    
    return redirect('home')

