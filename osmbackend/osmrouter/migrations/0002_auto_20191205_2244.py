# Generated by Django 3.0 on 2019-12-05 22:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('osmrouter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osmroutermodel',
            name='date_searched',
            field=models.DateField(default=datetime.datetime(2019, 12, 5, 22, 44, 37, 904714, tzinfo=utc)),
        ),
    ]