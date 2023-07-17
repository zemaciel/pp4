from django.db import models
from django.contrib.auth.models import User

# Create your models here.


TIME = (
    ('11:00', '11:00'),
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('17:00', '17:00'),
    ('17:30', '17:30'),
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19:00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
    ('21:00', '21:00'),
)


class RestaurantTable(models.Model):
    number = models.IntegerField(unique=True)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.CharField(max_length=20, choices=TIME, default='18:00')
    guests = models.IntegerField(max_length=2, default='2')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('table', 'date', 'time')

    def __str__(self):
        return str(self.name)
