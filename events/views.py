from django.shortcuts import render, redirect
from django.utils.dateparse import parse_date
from django.contrib import messages

from dashboard.forms import UserAttendeeForm
from dashboard.models import Attendee

def index(request):
    return render(request, 'events/index.html', {})

# Add accepted/not accepted
def apply(request):
    if request.method == 'POST':
        form = UserAttendeeForm(data=request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'You have applied successfully. We will get back to you soon.')
            return redirect('index')
    else:
        form = UserAttendeeForm()
    
    return render(request, 'events/apply.html', {'form': form})

def program(request):
    return render(request, 'events/program.html', {})