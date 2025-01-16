from django.db import models
from datetime import date
from django.core.management.base import BaseCommand
import uuid

class Attendee(models.Model):
    """
    Represents a person attending the event.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Personal Details
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        NONBINARY = 'NB', 'Non-Binary' 
        GENDERQUEER = 'GQ', 'Gender Queer'
        GENDERFLUID = 'GF', 'Gender Fluid' 
        OTHER = 'O', 'Other'

    class Medium(models.TextChoices):
        REFERRAL = 'R', 'Referral'
        ORGANIZATION_INSTITUTE = 'OI', 'Organization/Institution'
        EMAIL = 'E', 'Email Advertisement'
        SOCIAL_MEDIA = 'S', 'Social Media'
        OTHER = 'O', 'Other'


    YES_NO = (('Y', 'Yes'), ('N', 'No'))

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    gender = models.CharField(max_length=2,
        choices=Gender.choices,
        default=Gender.OTHER,
    )
    dob = models.DateField(blank=False, null=True, verbose_name="Date of Birth")
    
    # Name of organization/educational institute/community
    name_oec = models.CharField(max_length=150, verbose_name="Name of organization/educational institute/community")

    role = models.CharField(max_length=100, verbose_name="Role/Title")
    country = models.CharField(max_length=100, verbose_name="Nationality")
    country_residence = models.CharField(max_length=100, verbose_name="Country of Residence")
    linkedin = models.URLField(max_length=200)

    # Logistics
    virtual = models.CharField(max_length=1,
        choices=YES_NO,
        verbose_name="Attending Virtually",
    )
    # If they need a support letter or not
    support_letter = models.CharField(max_length=1,
        choices=YES_NO,
    )
    # How they heard about the conference
    medium = models.CharField(
        max_length=2,
        choices=Medium.choices,
        default=Medium.OTHER
    )

    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def age(self):
        today = date.today()
        if self.dob is None:
            return None
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
    
