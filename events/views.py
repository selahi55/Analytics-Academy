from django.shortcuts import render, redirect
from django.utils.dateparse import parse_date
from django.contrib import messages

from dashboard.forms import AttendeeForm
from dashboard.models import Attendee

def index(request):
    return render(request, 'events/index.html', {})

def apply(request):
    if request.method == 'POST':
        form = AttendeeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendees')
    else:
        form = AttendeeForm()
    # if request.method == "POST":
    #     email = request.POST.get("email")
    #     full_name = request.POST.get("full-name")
    #     gender = request.POST.get("gender")
    #     dob = parse_date(request.POST.get("dob"))
    #     nationality = request.POST.get("nationality")
    #     organization = request.POST.get("organization")
    #     role = request.POST.get("role")
    #     residence = request.POST.get("residence")
    #     linkedin = request.POST.get("linkedin", "")
    #     attending_virtually = request.POST.get("attending-virtually")
    #     visa_support = request.POST.get("visa-support")
    #     referral = request.POST.get("referral")

    #     try:
    #         first_name, last_name = full_name.split(' ', 1)
    #     except ValueError:
    #         first_name = full_name
    #         last_name = ""

    #     if gender == "Prefer-not-to-say":
    #         gender = "O"

    #     # Save data to the database
    #     attendee = Attendee(
    #         email=email,
    #         first_name=first_name,
    #         last_name=last_name,
    #         gender=gender,
    #         dob=dob,
    #         country=nationality,
    #         country_residence=residence,
    #         name_oec=organization,
    #         role=role,
    #         linkedin=linkedin,
    #         virtual='Y' if attending_virtually == "Yes" else 'N',
    #         support_letter='Y' if visa_support == "Yes" else 'N',
    #         medium=referral[0].upper() if referral else 'O',
    #     )
    #     attendee.save()
    #     messages.success(request,'Email sent successfully.')
    #     return redirect("apply")
    return render(request, 'events/apply.html', {'form': form})

def program(request):
    return render(request, 'events/program.html', {})