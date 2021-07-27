from django.db import models
import datetime


class StockQuery(models.Model):
    class StockCompanyName(models.TextChoices):
        ALLEGRO = 'ALE'
        CDPROJECT = 'CDR'
        PKNORLEN = 'PKN'
    company_name = models.CharField(max_length=20, choices=StockCompanyName.choices)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField()


class Companies(models.Model):
    name = models.TextField(db_column='NAME', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COMPANIES'


class Stock(models.Model):
    company_id = models.IntegerField(db_column='COMPANY_ID')  # Field name made lowercase.
    date = models.TextField(db_column='DATE')  # Field name made lowercase.
    open_price = models.FloatField(db_column='OPEN_PRICE')  # Field name made lowercase.
    max_price = models.FloatField(db_column='MAX_PRICE')  # Field name made lowercase.
    min_price = models.IntegerField(db_column='MIN_PRICE')  # Field name made lowercase.
    close_price = models.FloatField(db_column='CLOSE_PRICE')  # Field name made lowercase.
    volume = models.IntegerField(db_column='VOLUME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STOCK'
