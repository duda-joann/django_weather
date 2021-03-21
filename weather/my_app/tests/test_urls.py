from django.test import SimpleTestCase
from django.urls import (reverse,
                         resolve)
from my_app.views import index, delete_city


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('')
        self.assertEqual(resolve(url).func, index)

    def test_delete_city_is_resolved(self):
        url = reverse('delete', args=['city'])
        self.assertEquals(resolve(url).func, delete_city)


