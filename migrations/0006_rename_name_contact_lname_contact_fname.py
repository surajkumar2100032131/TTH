# Generated by Django 4.1.7 on 2023-03-31 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_contact_comment_signup_c_password_signup_mobile_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='lname',
        ),
        migrations.AddField(
            model_name='contact',
            name='fname',
            field=models.CharField(default='some', max_length=12),
        ),
    ]
