from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
from django.db.models import Count, F, Avg
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

from collections import Counter

from .models import Attendee
from .forms import EmailAttendee, AttendeeForm, EmailAttendees

@login_required(login_url='login')
def admin_dashboard(request):
    attendees = Attendee.objects.order_by('registered_at')
    ages = [attendee.age for attendee in attendees]
    intervals = [(10, 25), (25, 40), (40, 55), (55, 70), (70, 85), (85, 100)]
    interval_counts = {f"{start}-{end}": 0 for start, end in intervals}
    for age in ages:
        for start, end in intervals:
            if start <= age < end:
                interval_counts[f"{start}-{end}"] += 1
                break
    age_distribution = [{'age': key, 'count': value} for key, value in interval_counts.items()]

    genders = [attendee.gender for attendee in attendees]
    gender_counts = Counter(genders)
    gender_distribution = [{'gender': key, 'count': value} for key, value in gender_counts.items()]

    country = [attendee.country for attendee in attendees]
    country_counts = Counter(country)
    nationality_distribution = [{'country': key, 'count': value} for key, value in country_counts.most_common(5)]

    average_age = sum(ages)/len(ages) if len(ages) > 1 else ages
    total_attendees = Attendee.objects.all().count()
    total_amount = Attendee.objects.filter(paid="Y").count() * 100
    pop_nationality = attendees.values('country').annotate(count=Count('country')).order_by('-count').first()['country']
    unaccepted = attendees.filter(accepted="N").count()

    return render(request, 'dashboard/admin_dashboard.html', {"attendees": attendees,
                                                              "age_distribution": age_distribution,
                                                              "gender_distribution": gender_distribution,
                                                              "average_age": average_age,
                                                              "total_attendees": total_attendees,
                                                              "total_amount": total_amount,
                                                              "pop_nationality": pop_nationality,
                                                              "country_distribution": nationality_distribution,
                                                              "unaccepted": unaccepted})

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
def email_attendee(request, id):
    attendee = get_object_or_404(Attendee, id=id)

    if request.method == 'POST':
        form = EmailAttendee(data=request)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                settings.DEFAULT_FROM_MAIL,
                [attendee.email],
            )
            return redirect('dashboard')
    else:
        form = EmailAttendee()
    return render(request, 'dashboard/email_attendee.html', {'form': form,
                                                             'attendee': attendee})

@staff_member_required
def email_attendees(request):
    if request.method == 'POST':
        form = EmailAttendees(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            recipient_list = [attendee.email for attendee in cd['to_email']]
            send_mail(
                subject=cd['subject'],
                message=cd['message'],
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=recipient_list,
            )
            return redirect('dashboard')
    else:
        form = EmailAttendees()
    return render(request, 'dashboard/email_all.html', {'form': form})
