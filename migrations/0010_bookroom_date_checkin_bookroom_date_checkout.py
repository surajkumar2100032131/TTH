# Generated by Django 4.1.7 on 2023-04-01 20:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_bookroom_room_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookroom',
            name='Date_checkin',
            field=models.DateField(default=datetime.datetime(2023, 4, 2, 2, 12, 53, 753873), verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='bookroom',
            name='Date_checkout',
            field=models.DateField(default=datetime.datetime(2023, 4, 2, 2, 12, 53, 753873), verbose_name='Date'),
        ),
    ]
