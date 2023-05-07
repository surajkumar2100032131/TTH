# Generated by Django 4.1.7 on 2023-04-02 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_alter_bookroom_date_checkin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookroom',
            name='Date_checkin',
            field=models.DateField(default=datetime.datetime(2023, 4, 2, 23, 54, 42, 23471), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='bookroom',
            name='Date_checkout',
            field=models.DateField(default=datetime.datetime(2023, 4, 2, 23, 54, 42, 23471), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='bus',
            name='Children',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='bus',
            name='Date',
            field=models.DateField(default=datetime.datetime(2023, 4, 2, 23, 54, 42, 24465), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Date',
            field=models.DateField(default=datetime.datetime(2023, 4, 2, 23, 54, 42, 24465), verbose_name='Date'),
        ),
    ]