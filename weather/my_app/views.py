import requests
from django import http
from django.views.decorators.cache import cache_page
from django.shortcuts import render, redirect
from django.conf import settings
from .models import City
from .forms import CityForm
from .utils import get_weather


@cache_page(60 * 15)
def index(request : http.request) -> http.response:
    """
    render main page with weather
    """
    url = settings.API_URL

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

    weather_data = get_weather()

    context = {
        'weather_data' : weather_data, 
        'form' : form,
        'message' : message,
        'message_class' : message_class
    }

    return render(request, 'weather.html', context)


def delete_city(request: http.request, city_name: str) -> http.response:
    """
    Delete a choosen city by the user
    """

    City.objects.get(name=city_name).delete()
    
    return redirect('main')

