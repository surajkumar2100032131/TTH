# Generated by Django 4.1.7 on 2023-04-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_hotelcontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='some', max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(default='some', max_length=12)),
            ],
        ),
    ]