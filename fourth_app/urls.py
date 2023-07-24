from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('booking/', views.booking_page, name='booking_page'),
    path('mybookings/', views.mybookings_page, name='mybookings_page'),
    path('changebooking/<booking_id>', views.edit_booking, name='edit'),
    path('deletebooking/<booking_id>', views.delete_booking, name='delete'),
]
