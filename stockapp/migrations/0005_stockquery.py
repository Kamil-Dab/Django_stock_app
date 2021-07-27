# Generated by Django 3.2.5 on 2021-07-26 18:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stockapp', '0004_delete_stockquery'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(choices=[('ALE', 'Allegro'), ('CDR', 'Cdproject'), ('PKN', 'Pknorlen')], max_length=20)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField()),
            ],
        ),
    ]
