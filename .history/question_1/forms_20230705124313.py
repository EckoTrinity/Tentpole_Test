from django import forms
from bootstrap_datepicker_plus import DatePickerInput

# Create a template for the form

class FormName(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    date_of_birth = forms.DateField(widget=DatePickerInput(format='%m/%d/%Y'))
    statement_file = forms.FileField()