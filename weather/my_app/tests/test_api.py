import unittest
from unittest.mock import Mock, patch

from django.conf import settings
import requests
from ..utils import get_weather, get_api


class TestApiURL(unittest.TestCase):

    def setUp(self):
        self.params = {
            'q': 'London',
            'units': 'metric',
            'appid': settings.API_KEY
        }
        self.response = requests.get(settings.API_URL, params=self.params)
        self.weather = [{
          "weather": [
            {
              "id": 800,
              "main": "Clear",
              "description": "clear sky",
              "icon": "01d"
            }
          ],
          "base": "stations",
          "main": {
            "temp": 282.55,
            "feels_like": 281.86,
            "temp_min": 280.37,
            "temp_max": 284.26,
            "pressure": 1023,
            "humidity": 100
          }}]

    def test_api_url(self):
        self.assertEqual(self.response.status_code, 200)

    @patch('my_app.utils.requests.get')
    def test_getting_weather(self, mock_get):
        mock_get.return_value.ok = True
        self.assertIsNotNone(self.response)

    @patch('my_app.utils.requests.get')
    def test_getting_weather_when_response_ok(self, mock_get):
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = self.weather
        get_current_weather = get_api('Paris')
        self.assertListEqual(get_current_weather.json(), self.weather)


