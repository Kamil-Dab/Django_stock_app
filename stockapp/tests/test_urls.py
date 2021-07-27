from django.test import SimpleTestCase
from django.urls import reverse, resolve
from stockapp.views import home, stock_app


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolves(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)

    def test_stock_app_url_is_resolves(self):
        url = reverse('stock_app')
        print(resolve(url))
        self.assertEquals(resolve(url).func, stock_app)
