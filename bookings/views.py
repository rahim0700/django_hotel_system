from django.shortcuts import render, redirect
from .models import Room, Guest
from .forms import GuestRegistrationForm
from django.shortcuts import render, get_object_or_404
from .models import Guest, Booking
from .forms import CheckInForm
from django.utils import timezone

def room_list(request):
    all_rooms = Room.objects.all() 
    return render(request, 'room_list.html', {'rooms': all_rooms})

def register_guest(request):
    if request.method == 'POST':
        form = GuestRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') # Go back to the room list after saving
    else:
        form = GuestRegistrationForm()
    
    return render(request, 'register_guest.html', {'form': form})

def check_in_guest(request):
    if request.method == 'POST':
        form = CheckInForm(request.POST)
        if form.is_valid():
            booking = form.save()
            # Automatically update the room status
            room = booking.room
            room.room_status = 'Occupied'
            room.save()
            return redirect('home')
    else:
        form = CheckInForm()
    return render(request, 'check_in.html', {'form': form})

def guest_detail(request, guest_id):
    # This fetches the specific guest or shows a 404 error if they don't exist
    guest = get_object_or_404(Guest, id=guest_id)
    
    # This finds all bookings related to this guest
    history = Booking.objects.filter(guest=guest).order_by('-check_in')
    
    return render(request, 'guest_detail.html', {
        'guest': guest,
        'history': history
    })

def check_out_guest(request, booking_id):
    # Get the specific booking
    booking = get_object_or_404(Booking, id=booking_id)
    
    if request.method == 'POST':
        booking.check_out = timezone.now()
        booking.is_active = False
        booking.save()
        
        room = booking.room
        room.room_status = 'Available'
        room.save()
        
        return redirect('home')
    
    return render(request, 'check_out_confirmation.html', {'booking': booking})