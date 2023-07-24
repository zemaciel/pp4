# forms.py
from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name'}),
    )

    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'name@example.com'}),
    )

    phone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '+123456789'}),
    )

    class Meta:
        model = Booking
        fields = ('name', 'email', 'phone', 'table', 'date', 'time', 'guests')
        widgets = {
            'date': DateInput(),
        }
