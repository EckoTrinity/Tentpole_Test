from django import forms
from tempus_dominus.widgets import DatePicker

# Create a template for the form

class FormName(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    date_of_birth = forms.DateField(widget=DatePicker(
            options={
                'format': 'MM/DD/YYYY',
                'useCurrent': True,
                'collapse': False,
            }
        ))
    statement_file = forms.FileField()