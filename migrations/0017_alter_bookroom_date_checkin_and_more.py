# Generated by Django 4.1.7 on 2023-04-02 05:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_alter_bookroom_date_checkin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookroom',
            name='Date_checkin',
            field=models.DateField(default=datetime.datetime(2023, 4, 2, 11, 8, 13, 698646), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='bookroom',
            name='Date_checkout',
            field=models.DateField(default=datetime.datetime(2023, 4, 2, 11, 8, 13, 698646), verbose_name='Date'),
        ),
    ]