from django import forms
from .models import Booking, Guest, Room
from .models import Booking
class GuestRegistrationForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['first_name', 'last_name', 'contact']

class CheckInForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['guest', 'room']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['room'].queryset = Room.objects.filter(room_status='Available')