from django.db import migrations, models

class Room(models.Model):
    ROOM_TYPES = [('Single', 'Single'), ('Double', 'Double'), ('VIP', 'VIP')]
    STATUS_CHOICES = [('Available', 'Available'), ('Occupied', 'Occupied')]

    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    room_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type})"

class Guest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Booking(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField(auto_now_add=True)
    check_out = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.guest} in {self.room}"