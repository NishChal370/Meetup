from django import forms
from .models import Participant

class RegistrationForms(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['email']