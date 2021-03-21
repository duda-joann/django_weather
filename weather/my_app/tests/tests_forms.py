from django.test import SimpleTestCase
from my_app.forms import CityForm
from my_app.models import City


class TestForms(SimpleTestCase):

    def test_city_form_valid_data(self):
        form = CityForm(data={
            'city': 'Budapest',
        })

        self.assertTrue(form.is_valid())

    def test_city_form_no_data(self):
        form = CityForm(data={})
        self.assertFalse(form.is_valid())

    def test_city_form_incorrect_data(self):
        form = CityForm(data={
            'city': "PiernikowoWielkieNieWiemGdzie"
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, 'City does not exist in the world!')

    def test_city_form_city_exist(self):

        form = CityForm(data={})