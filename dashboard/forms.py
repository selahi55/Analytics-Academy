from django import forms
from datetime import date
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

from .models import Attendee
from .countries import COUNTRY_CHOICES

class DateInput(forms.DateInput):
    input_type = 'date'

class UserAttendeeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['virtual'].label = "Will you be attending virtually?"
        self.fields['support_letter'].label = "Do you need a support letter for a visa to attend the NGUN at The Hague in May 2025?"
        self.fields['medium'].label = "How did you hear about the NGUN conference?"

        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter your first name.'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter your last name.'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email.'})
        self.fields['name_oec'].widget.attrs.update({'placeholder': 'Enter the name of your organization/institute/'})
        self.fields['role'].widget.attrs.update({'placeholder': 'Enter your role.'})
        self.fields['country'].widget.attrs.update({'placeholder': 'Enter your nationality.'})
        self.fields['country_residence'].widget.attrs.update({'placeholder': 'Enter your country of residence.'})
        self.fields['linkedin'].widget.attrs.update({'placeholder': 'Enter your linkedin URL.'})
        
        self.fields['country'].widget = forms.Select(choices=COUNTRY_CHOICES)
        self.fields['country_residence'].widget = forms.Select(choices=COUNTRY_CHOICES)
        
    class Meta:
        model = Attendee
        fields = ['email', 'first_name', 'last_name', 
                  'gender', 'dob', 'name_oec', 'role', 
                  'country', 'country_residence', 'linkedin', 
                  'virtual', 'support_letter', 'medium']
        widgets = {
            'dob': DateInput(),
        }

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if dob:
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age < 15:
                raise ValidationError("The date of birth indicates an age less than 15 years.")
        return dob


class AttendeeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['virtual'].label = "Will you be attending virtually?"
        self.fields['support_letter'].label = "Do you need a support letter for a visa to attend the NGUN at The Hague in May 2025?"
        self.fields['medium'].label = "How did you hear about the NGUN conference?"

        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter your first name.'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter your last name.'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email.'})
        self.fields['name_oec'].widget.attrs.update({'placeholder': 'Enter the name of your organization/institute/'})
        self.fields['role'].widget.attrs.update({'placeholder': 'Enter your role.'})
        self.fields['country'].widget.attrs.update({'placeholder': 'Enter your nationality.'})
        self.fields['country_residence'].widget.attrs.update({'placeholder': 'Enter your country of residence.'})
        self.fields['linkedin'].widget.attrs.update({'placeholder': 'Enter your linkedin URL.'})
        
        self.fields['country'].widget = forms.Select(choices=COUNTRY_CHOICES)
        self.fields['country_residence'].widget = forms.Select(choices=COUNTRY_CHOICES)
        
    class Meta:
        model = Attendee
        fields = "__all__"
        widgets = {
            'dob': DateInput(),
        }

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if dob:
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age < 15:
                raise ValidationError("The date of birth indicates an age less than 15 years.")
        return dob

class EmailAttendee(forms.Form):
    to_email = forms.EmailField(label='Email', required=True, max_length=100)
    subject = forms.CharField(label='Subject', required=True, max_length=100)
    message = forms.CharField(label='Message', required=True, max_length=500, widget=forms.Textarea)
