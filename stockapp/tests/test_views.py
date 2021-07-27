from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from stockapp.models import StockQuery, Stock, Companies
import json


class TestViews(TestCase):
    databases = '__all__'

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.stock_app_url = reverse('stock_app')
        User.objects.create_superuser(
            username='superuser', password='secret', email='admin@example.com'
        )

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_stock_app_not_logged_GET(self):
        response = self.client.get(self.stock_app_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_stock_app_logged_GET(self):
        self.client.login(username='superuser', password='secret')
        response = self.client.get(self.stock_app_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock_app.html')

    def test_stock_app_POST_no_data(self):
        try:
            self.client.login(username='superuser', password='secret')
            response = self.client.post(self.stock_app_url)
        except KeyError:
            pass

