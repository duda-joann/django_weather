from django.test import SimpleTestCase
from ..forms import CityForm
from ..models import City


class TestForms(SimpleTestCase):

    def test_city_form_valid_data(self):
        form = CityForm(data={
            'name': 'Rome',
        })

        self.assertTrue(form.is_valid())

    def test_city_form_no_data(self):
        form = CityForm(data={})
        self.assertFalse(form.is_valid())

    def test_city_form_incorrect_data(self):
        form = CityForm(data={
            'name': "PiernikowoWielkieNieWiemGdzie"
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'name': ['Ensure this value has at most 25 characters (it has 29).']})

    def test_city_form_city_exist(self):
        form = CityForm(data={
            'name': 'Rome'
        })

