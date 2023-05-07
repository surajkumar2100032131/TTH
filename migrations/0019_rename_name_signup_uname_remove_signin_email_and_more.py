# Generated by Django 4.1.7 on 2023-04-02 17:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_alter_bookroom_date_checkin_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='name',
            new_name='uname',
        ),
        migrations.RemoveField(
            model_name='signin',
            name='email',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='mobile',
        ),
        migrations.AddField(
            model_name='signin',
            name='username',
            field=models.CharField(default='text', max_length=20),
        ),
        migrations.AlterField(
            model_name='bookroom',
            name='Date_checkin',
            field=models.DateField(default=datetime.datetime(2023, 4, 2, 22, 34, 55, 732945), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='bookroom',
            name='Date_checkout',
            field=models.DateField(default=datetime.datetime(2023, 4, 2, 22, 34, 55, 732945), verbose_name='Date'),
        ),
    ]
