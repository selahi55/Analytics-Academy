from django.core.management.base import BaseCommand
from dashboard.models import Attendee
from faker import Faker
import random

class Command(BaseCommand):
    help = "Generates dummy data and saves to model"

    def handle(self, *args, **options):
        fake = Faker()

        def generate_random_attendee():
            return Attendee(
                email=fake.email(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                gender=random.choice([Attendee.Gender.MALE, Attendee.Gender.FEMALE]),
                dob=fake.date_of_birth(),
                name_oec=fake.company(),
                role=fake.job(),
                country=fake.country(),
                country_residence=fake.country(),
                linkedin=fake.url(),
                virtual=random.choice(['Y', 'N']),
                support_letter=random.choice(['Y', 'N']),
                medium=random.choice(['R', 'E', 'S', 'O', 'OI'])
            )

        for _ in range(50):
            new_attendee = generate_random_attendee()
            new_attendee.save()

        self.stdout.write(self.style.SUCCESS('Successfully created dummy data for Attendee model'))