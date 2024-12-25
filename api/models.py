from django.db import models
from datetime import date
from django.core.management.base import BaseCommand

class Attendee(models.Model):
    """
    Represents a person attending the event.
    """
    # Personal Details
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        NONBINARY = 'NB', 'Non-Binary' 
        GENDERQUEER = 'GQ', 'Gender Queer'
        GENDERFLUID = 'GF', 'Gender Fluid' 
        OTHER = 'O', 'Other'

    YES_NO = (('Y', 'Yes'), ('N', 'No'))

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    gender = models.CharField(max_length=2,
        choices=Gender.choices,
        default=Gender.OTHER,
    )
    dob = models.DateField(blank=False, null=True)
    
    # Name of organization/educational institute/community
    name_oec = models.CharField(max_length=150)

    role = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    linkedin = models.URLField(max_length=200)

    # Logistics
    virtual = models.CharField(max_length=1,
        choices=YES_NO,
    )
    # If they need a support letter or not
    support_letter = models.CharField(max_length=1,
        choices=YES_NO,
    )
    # How they heard about the conference
    medium = models.CharField(max_length=300)

    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def age(self):
        today = date.today()
        if self.dob is None:
            return None
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
    
# class Command(BaseCommand):
#     help = 'Create dummy data for Attendee model'

#     def handle(self, *args, **kwargs):
#         attendees = [
#             Attendee(
#                 email='john.doe@example.com',
#                 first_name='John',
#                 last_name='Doe',
#                 gender=Attendee.Gender.MALE,
#                 dob=date(1990, 1, 1),
#                 name_oec='Example University',
#                 role='Student',
#                 country='USA',
#                 linkedin='https://www.linkedin.com/in/johndoe',
#                 virtual='Y',
#                 support_letter='N',
#                 medium='Social Media'
#             ),
#             Attendee(
#                 email='jane.smith@example.com',
#                 first_name='Jane',
#                 last_name='Smith',
#                 gender=Attendee.Gender.FEMALE,
#                 dob=date(1985, 5, 15),
#                 name_oec='Tech Corp',
#                 role='Engineer',
#                 country='Canada',
#                 linkedin='https://www.linkedin.com/in/janesmith',
#                 virtual='N',
#                 support_letter='Y',
#                 medium='Email'
#             ),
#         ]

#         for attendee in attendees:
#             attendee.save()

#         self.stdout.write(self.style.SUCCESS('Successfully created dummy data for Attendee model'))