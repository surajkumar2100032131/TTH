# Generated by Django 4.1.7 on 2023-05-06 22:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0029_alter_bookroom_date_checkin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookroom',
            name='Date_checkin',
            field=models.DateField(default=datetime.datetime(2023, 5, 7, 4, 18, 48, 988468), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='bookroom',
            name='Date_checkout',
            field=models.DateField(default=datetime.datetime(2023, 5, 7, 4, 18, 48, 988468), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='bus',
            name='Date',
            field=models.DateField(default=datetime.datetime(2023, 5, 7, 4, 18, 48, 989469), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='bus',
            name='economy',
            field=models.CharField(choices=[('BGN', 'Business'), ('FST', 'FIRST'), ('Ac', 'AC'), ('NAc', 'NON AC'), ('sl', 'SL'), ('lb', 'LB'), ('mb', 'MB'), ('ub', 'UB'), ('su', 'SU')], default='STND', max_length=10),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Date',
            field=models.DateField(default=datetime.datetime(2023, 5, 7, 4, 18, 48, 988468), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='flights',
            name='Date',
            field=models.DateField(default=datetime.datetime(2023, 5, 7, 4, 18, 48, 989469), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='flights',
            name='economy',
            field=models.CharField(choices=[('BGN', 'Business'), ('FST', 'FIRST'), ('Ac', 'AC'), ('NAc', 'NON AC'), ('sl', 'SL'), ('lb', 'LB'), ('mb', 'MB'), ('ub', 'UB'), ('su', 'SU')], default='STND', max_length=10),
        ),
    ]