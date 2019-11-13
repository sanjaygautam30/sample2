from django import forms
from .models import Passanger

class CreatePassangerForm(forms.ModelForm):
    class Meta:
        model=Passanger
        fields='__all__'

class DeletePassangerForm(forms.ModelForm):
    class Meta:
        model=Passanger
        fields=['pid']