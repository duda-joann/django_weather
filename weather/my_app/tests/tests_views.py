from django.test import TestCase, Client
from django.urls import reverse
from my_app.models import City
from my_app.views import index, delete_city


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.main_url = reverse('')
        self.delete_url = reverse('delete', args=['city'])

    def test_index_GET(self):
        response = self.client.get(self.main_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weather.html')

    def test_index_POST(self):
        pass