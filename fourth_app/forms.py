from django import forms
from .models import Booking

# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ('table', 'date', 'time', 'guests')


class DateInput(forms.DateInput):
#     """This class provides a widget that the user can
#     click on. It cretes a better UX when choosing the date
#     for the booking.
#     """
    input_type = 'date'


class BookingForm(forms.ModelForm):
#     """This class generates a form based on the fields in the
#     Booking model, except for the User field.
#     It will then be displayed in the Booking template
#     in order for the user to make their booking using the form.
#     """
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name'}),
    )

    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'name@example.com'}),
    )

    phone = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '+123456789'}),
    )

    class Meta:
        model = Booking
        exclude = ('user', )
        widgets = {
            'date': DateInput(),
        }