from django.test import TestCase
from stockapp.models import StockQuery, Stock, Companies


class TestModels(TestCase):

    def setUp(self):
        self.stock_query1 = StockQuery.objects.create(
            company_name='ALE',
            start_date='2020-12-12',
            end_date='2021-12-12'
        )
