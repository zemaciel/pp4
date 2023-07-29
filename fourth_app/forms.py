# forms.py
from django import forms
from .models import Booking
from django.utils import timezone


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

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < timezone.now().date():
            raise forms.ValidationError("Please, choose a future date.")
        return date
