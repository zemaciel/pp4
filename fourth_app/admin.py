from django.contrib import admin
from .models import Booking

# Register your models here.
# admin.site.register(Booking)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'created_on')
    list_filter = ('date',)
    search_fields = ('name', 'email')
