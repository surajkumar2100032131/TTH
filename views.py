from django.shortcuts import render, HttpResponse,redirect
from .models import Contact,Hotelcontact,Bookroom,Payment,Flight,Bus,Flights,Signin,Signup
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import os
from django.contrib import messages

def sample1(request):
    return render(request,"home.html")




def SignUp(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        c_password = request.POST.get('cpassword')
        if password != c_password:
            return render(request, "notcreatedaccount.html")
        else:
            my_user = User.objects.create_user(uname, email, password)
            my_user.save()
            return render(request, "accountcreated.html")
    return render(request, "signup.html")



def Home1(request):
    return render(request,"home1.html")

def SignIn(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:

            login(request, user)
            return redirect("/Home")
        else:
            return render(request, "notcorrect.html")

    return render(request, "signin.html")



def contact(request):
    if request.method=="POST":
        fname = request.POST.get("fn")
        lname = request.POST.get("ln")
        email=request.POST.get("email")
        phone=request.POST.get("ph")
        comment=request.POST.get("comm")
        contect=Contact(fname=fname,lname=lname,email=email,phone=phone,comment=comment)
        contect.save()
        return redirect('/')
    return render(request,"contact.html")





def travels(request):
    return render(request,"travel.html")


def tourisms(request):
    return render(request,"tourism.html")


def tts(request):
    return render(request,"tt.html")


def bloggers(request):
    return render(request,"blogger.html")


def hotels(request):
    return render(request,"hotel.html")


def abouthotels(request):
    return render(request,"abouthotel.html")




def know(request):
    return render(request,'know1.html')

def Aboutus(request):
    return render(request,'aboutus.html')

def room(request):
    return render(request,'bookroom.html')

def explore(request):
    return render(request,'explore.html')

def contact1(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email=request.POST.get("email")
        message = request.POST.get("message")
        contact=Hotelcontact(name=name,email=email,message=message)
        contact.save()
        return HttpResponse("Message has been sent successfully !!!!")
    return render(request,"contact1.html")

def bookroom(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        room_type=request.POST.get("room-type")
        Date_checkin=request.POST.get("check-in-date")
        Date_checkout = request.POST.get("check-out-date")
        book= Bookroom(name=name, email=email, phone=phone,room_type=room_type,Date_checkin=Date_checkin,Date_checkout=Date_checkout)
        book.save()
        return redirect('/flights')
    return render(request, "bookroom.html")


def explore1(request):
    return render(request, "explore1.html")

def payment(request):
    if request.method == "POST":
        amount = request.POST.get("number")
        card_name = request.POST.get("cardname")
        card_number = request.POST.get("cardnumber")
        Exp_month = request.POST.get("expmonth")
        Exp_year = request.POST.get("expyear")
        cvv = request.POST.get("cvv")
        pay =Payment(amount=amount, card_name=card_name,card_number=card_number, Exp_month=Exp_month, Exp_year=Exp_year,  cvv=cvv,)
        pay.save()
        return redirect('/psuccess')
    return render(request, "payment.html")


def flightbooking(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        Date = request.POST.get("date")
        economy = request.POST.get("eco")
        Adults = request.POST.get("number")
        Children = request.POST.get("number1")
        book = Flight(name=name, email=email, phone=phone,Date=Date,economy=economy, Adults=Adults, Children=Children)
        book.save()
        return redirect('/payments')
    return render(request, "flightbooking.html")

def flightbooking1(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        Date = request.POST.get("date")
        economy = request.POST.get("eco")
        Adults = request.POST.get("number")
        Children = request.POST.get("number1")
        book = Flights(name=name, email=email, phone=phone,Date=Date,economy=economy, Adults=Adults, Children=Children)
        book.save()
        return redirect("/payflight")
    return render(request, "flightbooking1.html")

def bus(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        Date = request.POST.get("date")
        economy = request.POST.get("eco")
        Adults = request.POST.get("number")
        Children = request.POST.get("number1")
        book = Bus(name=name, email=email, phone=phone,Date=Date, economy=economy, Adults=Adults, Children=Children)
        book.save()
        return redirect('/payments')
    return render(request, "bus.html")


def paymentflight(request):
    return render(request, "paymentflight.html")
def paymentbus(request):
    return render(request, "paymentbus.html")

def paymentsuccess(request):
    return render(request,"paymentsuccess.html")






