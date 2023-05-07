from django.contrib import admin
from django.urls import path, include
from .views import sample1,SignUp,Home1,SignIn,contact,travels,tourisms,tts,bloggers,hotels,abouthotels,contact1,know,Aboutus,room,explore,bookroom,explore1
from .views import payment,flightbooking,paymentsuccess,bus,paymentflight,paymentbus,flightbooking1
urlpatterns = [
   path('',sample1,name="sample1"),
   path('signup/',SignUp,name='rg'),
   path('Home/',Home1,name='h1'),
   path('signin/', SignIn, name='rg1'),
   path('contacts/',contact,name='ct'),
   path('travel',travels,name='ht'),
   path('tourism/',tourisms,name='tr'),
   path('tt/',tts,name='rec'),
   path('blog/',bloggers,name='bl'),
   path('hotel/',hotels,name='hl'),
   path('abouthotel/',abouthotels,name='ah'),
   path('contact/',contact1,name='co'),
   path('knowmore/',know),
   path('aboutus/',Aboutus),
   path('knowmore/Bookroom/',room),
   path('explore/',explore),
   path('bookrooms/',bookroom,name='br'),
   path('exploreroom/',explore1,name='er'),
   path('payments/',payment,name='pa'),
   path('flights/',flightbooking,name='fl'),
   path('psuccess/',paymentsuccess,name='ps'),
   path('buses/',bus,name='bs'),
   path('payflight/',paymentflight,name='pf'),
   path('paybus/',paymentbus,name='pb'),
   path('flights1/',flightbooking1,name='fb')

]