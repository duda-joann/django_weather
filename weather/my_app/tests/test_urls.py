from django.test import SimpleTestCase
from django.urls import (reverse,
                         resolve)
from ..views import index, delete_city


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        f = resolve('/main').func
        self.assertEqual(f.__name__, index.__name__)
        self.assertEqual(f.__module__, index.__module__)

    def test_delete_city_is_resolved(self):
        url = reverse('delete', args=['city'])
        self.assertEquals(resolve(url).func, delete_city)


