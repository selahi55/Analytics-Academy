from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required

from .models import Attendee
from .forms import EmailAttendee
from .forms import AttendeeForm 

@staff_member_required
def admin_dashboard(request):
    attendees = Attendee.objects.all()
    return render(request, 'dashboard/admin_dashboard.html', {"attendees": attendees})

@staff_member_required
def attendees(request):
    attendees = Attendee.objects.all()
    fields = [
        {'name': field.name, 'verbose_name': field.verbose_name}
        for field in Attendee._meta.get_fields()
        if hasattr(field, 'verbose_name')  # Ensures it's a database field
    ]    
    return render(request, 'dashboard/attendees.html', {"attendees": attendees,
                                                        "fields": fields})

@staff_member_required
def add_attendee(request):
    if request.method == 'POST':
        form = AttendeeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendees')
    else:
        form = AttendeeForm()
    return render(request, 'dashboard/add_attendee.html', {'form': form})

@staff_member_required
def attendee_detail(request, id):
    attendee = get_object_or_404(Attendee, id=id)
    fields = [
        {'name': field.name, 'verbose_name': field.verbose_name}
        for field in Attendee._meta.get_fields()
        if hasattr(field, 'verbose_name')
    ]    
    return render(request, 'dashboard/attendee_detail.html', {"attendee": attendee,
                                                              "fields": fields})

@staff_member_required
def edit_attendee(request, id):
    instance = get_object_or_404(Attendee, id=id)
    if request.method == 'POST':
        form = AttendeeForm(data=request.POST, instance=instance)
        if form.is_valid():
            instance.save()
            return redirect('attendees')
    else:
        form = AttendeeForm(instance=instance)
    return render(request, 'dashboard/update_attendee.html', {'form': form,
                                                              'instance': instance})

@staff_member_required
def delete_attendee(request, id):
    attendee = get_object_or_404(Attendee, id=id)

    if request.method == 'POST':
        attendee.delete()
        return redirect('attendees')
    else:
        fields = [
        {'name': field.name, 'verbose_name': field.verbose_name}
        for field in Attendee._meta.get_fields()
        if hasattr(field, 'verbose_name')
        ]       
        return render(request, 'dashboard/delete_attendee.html', {'attendee': attendee,
                                                                  "fields": fields})

@staff_member_required
def send_mail_to_attendee(request, id):
    attendee = get_object_or_404(Attendee, id=id)

    if request.method == 'POST':
        form = EmailAttendee(data=request.POST)
        if form.is_valid():
            cd   = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                settings.DEFAULT_FROM_MAIL,
                [attendee.email],
                fail_silently=False,
            )
            messages.success(request,'Email sent successfully.')
            return redirect('dashboard')
    else:
        form = EmailAttendee()  
    return render(request, 'dashboard/email_attendee.html', {'form': form,
                                                          'attendee': attendee})

