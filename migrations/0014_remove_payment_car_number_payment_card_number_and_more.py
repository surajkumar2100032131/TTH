# Generated by Django 4.1.7 on 2023-04-02 02:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_alter_bookroom_date_checkin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='car_number',
        ),
        migrations.AddField(
            model_name='payment',
            name='card_number',
            field=models.CharField(default='some', max_length=15),
        ),
        migrations.AlterField(
            model_name='bookroom',
            name='Date_checkin',
            field=models.DateField(default=datetime.datetime(2023, 4, 2, 8, 22, 4, 136092), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='bookroom',
            name='Date_checkout',
            field=models.DateField(default=datetime.datetime(2023, 4, 2, 8, 22, 4, 136092), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='Exp_year',
            field=models.CharField(default='some', max_length=30),
        ),
    ]
