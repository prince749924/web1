from django.urls import path
from booking import views

urlpatterns = [
    path('bookingnew/<int:id>',views.bookingnew),
    path('bookingfinal',views.bookingfinal, name='booking'),
    path('bookingview',views.bookingview),


]