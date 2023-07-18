from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Booking
from .forms import BookingForm
from django.contrib import messages

def home(request):
    """The view for the start page. Renders the index.html
    page which also extends the base.html
    """
    return render(request, 'index.html')


def booking_page(request):
    """The view for the booking page. If user is logged in it renders the
    booking.html, otherwise it renders the page to login or signup.
    When user has made a booking it redirects to mybooking overview page.
    It takes the input from the form and store it in the Booking model.
    """
    if request.method == 'POST':
        form = BookingForm(data=request.POST)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.user = request.user
            booking_form.save()
            messages.success(request, 'Booking is confirmed')
            return redirect('mybookings_page')
        else:
            messages.error(
                request, 'Invalid, incorrect info or double booking')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'booking.html', context)


def mybookings_page(request):
    """The view that renders the mybookings.html which shows all
    current booking by the user. Checks if user is logged in
    otherwise it redirects to the signup page.
    """
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user=request.user)
        context = {
           'bookings': bookings
        }
        return render(request, 'mybookings.html', context)
    else:
        return redirect('../accounts/signup')


def edit_booking(request, booking_id):
    """The view that renders the edit_booking page where the user can
    update a current booking. Checks if current user matches the user
    that made the booking, otherwise it redirects to the mybookings_page.
    Uses the form data from the user to update the booking in the database.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if request.user != booking.user:
        return redirect('mybookings_page')
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking has been updated')
            return redirect('mybookings_page')
    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'update_booking.html', context)


def delete_booking(request, booking_id):
    """The view that performs the deletion of a booking.
    Checks if current user matches the user that made the booking,
    otherwise it redirects to the mybookings_page.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if request.user != booking.user:
        return redirect('mybookings_page')
    booking.delete()
    messages.success(request, 'Booking has been deleted')
    return redirect('mybookings_page')