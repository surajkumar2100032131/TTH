# Generated by Django 4.1.7 on 2023-04-02 02:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_bookroom_date_checkin_bookroom_date_checkout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('card_name', models.CharField(default='some', max_length=20)),
                ('car_number', models.IntegerField()),
                ('Exp_month', models.CharField(default='some', max_length=30)),
                ('Exp_year', models.IntegerField()),
                ('cvv', models.CharField(default='some', max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='bookroom',
            name='Date_checkin',
            field=models.DateField(default=datetime.datetime(2023, 4, 2, 7, 43, 7, 546457), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='bookroom',
            name='Date_checkout',
            field=models.DateField(default=datetime.datetime(2023, 4, 2, 7, 43, 7, 546457), verbose_name='Date'),
        ),
    ]
