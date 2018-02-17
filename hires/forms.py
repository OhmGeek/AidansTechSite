from django import forms
from .models import Hire
from django.forms import DateInput

class HireCreateForm(forms.ModelForm):
    class Meta:
        model = Hire
        fields = ['booking_name', 'hirer_name', 'invoice_name', 'email_address', 'date_out', 'date_in', 'contact_number']
        widgets = {
            'date_in': DateInput(attrs={'type': 'date'}),
            'date_out': DateInput(attrs={'type': 'date'}),
        }
