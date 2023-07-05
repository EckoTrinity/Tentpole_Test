from django import forms

# Create custom widget in your forms.py file.
class DateInput(forms.DateInput):
    input_type = 'date'

# Create a template for the form

class FormName(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    date_of_birth = forms.DateField(widget=DateInput)
    statement_file = forms.FileField()
