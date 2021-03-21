from django.test import TestCase
from my_app.models import City, CityWeather
import datetime


datetime.datetime.now = lambda: datetime.datetime(2021, 3, 21)


class TestCityModel(TestCase):

    def setUp(self):
        self.city = City.objects.create(name='London')

    def test_city_object_is_created(self):
        obj = City.objects.all()
        self.assertEqual(len(obj),1)

    def test_city_label(self):
        city_db = City.objects.get(id=1)
        field_label = city_db.__meta.get_field('name').verbose_name
        self.assertEqual(self.city, field_label)

    def test_city_length(self):
        city_db = City.objects.get(id=1)
        max_length = city_db._meta.get_field('name').max_length
        self.assertEqual(max_length,25)


class TestCityWeatherModel(TestCase):
    def setUp(self):
        self.city = CityWeather.objects.create(
            city =self.city,
            temperature = '2',
            description = 'snowy, windy weather',
            icon = 'www.openweather.com/wethear/icon',
            date = datetime.datetime.now)

    def test_city_weather_obj(self):
        obj= CityWeather.objects.all()
        self.assertEqual(len(obj), 1)

    def test_test_city_label(self):
        city_db = City.objects.get(id=1)
        field_label = city_db.__meta.get_field('city').verbose_name
        self.assertEqual(self.city, field_label)

    def test_temperature_label(self):
        city_db = City.objects.get(id=1)
        field_label = city_db.__meta.get_field('temperature').verbose_name
        self.assertEqual('2', field_label)

    def test_descriptions_label(self):
        city_db = City.objects.get(id=1)
        field_label = city_db.__meta.get_field('descriptions').verbose_name
        self.assertEqual('snowy, windy weather', field_label)

    def test_icon_label(self):
        city_db = City.objects.get(id=1)
        field_label = city_db.__meta.get_field('icon').verbose_name
        self.assertEqual('www.openweather.com/wethear/icon', field_label)

    def test_date_label(self):
        city_db = City.objects.get(id=1)
        field_label = city_db.__meta.get_field('date').verbose_name
        self.assertEqual('2021-03-21', field_label)

