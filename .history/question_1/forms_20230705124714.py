from django import forms
from datepicker.widgets import DatePicker

# Create a template for the form

class FormName(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    date_of_birth = forms.DateField(options={"format": "mm/dd/yyyy"})
    statement_file = forms.FileField()