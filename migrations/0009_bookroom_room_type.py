# Generated by Django 4.1.7 on 2023-04-01 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_bookroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookroom',
            name='room_type',
            field=models.CharField(choices=[('SGL', 'Single'), ('DBL', 'Double'), ('DLX', 'Deluxe')], default='STND', max_length=10),
        ),
    ]
