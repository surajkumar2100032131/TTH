from django.db import models
from datetime import datetime

# makemigrations - create changes and store in a file
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Signin(models.Model):
    username=models.CharField(max_length=20,default='text')
    password=models.CharField(max_length=15)

class Signup(models.Model):
    uname=models.CharField(max_length=20,default='some')
    email=models.EmailField()
    password=models.CharField(max_length=15,default='some')
    c_password=models.CharField(max_length=15, default='some')




class Contact(models.Model):
    fname=models.CharField(max_length=12,default='some')
    lname = models.CharField(max_length=20,default='some')
    email = models.EmailField()
    phone=models.CharField(max_length=12,default='some')
    comment=models.CharField(max_length=140, default='SOME STRING')

class Hotelcontact(models.Model):
    name = models.CharField(max_length=12, default='some')
    email = models.EmailField()
    message = models.CharField(max_length=150, default='some')


class Bookroom(models.Model):
    name = models.CharField(max_length=12, default='some')
    email = models.EmailField()
    phone = models.CharField(max_length=12, default='some')
    ROOM_TYPES = (
        ('SGL', 'Single'),
        ('DBL', 'Double'),
        ('DLX', 'Deluxe'),
    )
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES, default="STND")
    Date_checkin = models.DateField(("Date"), default=datetime.now())
    Date_checkout = models.DateField(("Date"), default=datetime.now())


class Payment(models.Model):
    amount=models.IntegerField()
    card_name = models.CharField(max_length=20,default='some')
    card_number = models.CharField(max_length=15,default='some')
    Exp_month=models.CharField(max_length=30,default='some')
    Exp_year=models.CharField(max_length=30,default='some')
    cvv=models.CharField(max_length=15,default='some')

class Flight(models.Model):
    name = models.CharField(max_length=12, default='some')
    email = models.EmailField()
    phone = models.CharField(max_length=12, default='some')
    Date = models.DateField(("Date"), default=datetime.now())
    Economy = (
        ('BGN', 'Business'),
        ('FST', 'FIRST'),
    )
    economy = models.CharField(max_length=10, choices=Economy, default="STND")
    Adults = models.CharField(max_length=12, default='some')
    Children = models.CharField(max_length=12, default='some')

class Flights(models.Model):
    name = models.CharField(max_length=12, default='some')
    email = models.EmailField()
    phone = models.CharField(max_length=12, default='some')
    Date = models.DateField(("Date"), default=datetime.now())
    Economy = (
        ('BGN', 'Business'),
        ('FST', 'FIRST'),
        ('Ac', 'AC'),
        ('NAc', 'NON AC'),
        ('sl', 'SL'),
        ('lb', 'LB'),
        ('mb', 'MB'),
        ('ub', 'UB'),
        ('su', 'SU'),
    )
    economy = models.CharField(max_length=10, choices=Economy, default="STND")
    Adults = models.CharField(max_length=12, default='some')
    Children = models.CharField(max_length=12, default='some')


class Bus(models.Model):
    name = models.CharField(max_length=12, default='some')
    email = models.EmailField()
    phone = models.CharField(max_length=12, default='some')
    Date = models.DateField(("Date"), default=datetime.now())
    Economy = (
        ('BGN', 'Business'),
        ('FST', 'FIRST'),
        ('Ac', 'AC'),
        ('NAc', 'NON AC'),
        ('sl', 'SL'),
        ('lb', 'LB'),
        ('mb', 'MB'),
        ('ub', 'UB'),
        ('su', 'SU'),
    )
    economy = models.CharField(max_length=10, choices=Economy, default="STND")
    Adults = models.CharField(max_length=12, default='some')
    Children = models.CharField(max_length=12,null=True)












