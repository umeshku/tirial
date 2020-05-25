from django import forms
from django.forms import ModelForm
from .models import Household, Personal
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput

class HouseholdForm(forms.ModelForm):

    class Meta:
        model=Household
        fields='__all__'

        widgets = {
        'SubmissionDate':DateTimePickerInput(),
        'start':DateTimePickerInput(),
        'end':DateTimePickerInput(),
        }

class PersonalForm(forms.ModelForm):
    class Meta:
        model=Personal
        exclude = ['PARENT_KEY']
