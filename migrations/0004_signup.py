# Generated by Django 4.1.7 on 2023-03-31 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_signin_alter_contact_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]