from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Booking, RestaurantTable  
from .forms import BookingForm

def home(request):
    return render(request, 'index.html')

# Page to create a new booking
def booking_page(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
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


# Page showing the users bookings

def mybookings_page(request):
   
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user=request.user)
        context = {
           'bookings': bookings
        }
        return render(request, 'mybookings.html', context)
    else:
        return redirect('../accounts/signup')

# view to the edit_booking page - to update a exisiting booking

def edit_booking(request, booking_id):

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


