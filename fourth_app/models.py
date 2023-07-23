from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TABLEAREA = (
    ('Indoors', 'Indoors'),
    ('Outdoors', 'Outdoors'),
)

GUESTNUMBER = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
)


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

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=75, default='')
    email = models.EmailField(default='')
    phone = models.CharField(max_length=20, default='')
    table = models.CharField(max_length=12, choices=TABLEAREA, default='Indoors', null=True)
    date = models.DateField()
    time = models.CharField(max_length=20, choices=TIME, default='18:00')
    guests = models.CharField(max_length=2, choices=GUESTNUMBER, default='2')
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('table', 'date', 'time')

    def __str__(self):
        return f"{self.user.username} - {self.table} - {self.date}"
