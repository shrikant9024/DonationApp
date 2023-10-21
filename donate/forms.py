from django import forms
from .models import charity


class DonationForm(forms.ModelForm):
    class Meta:
        model = charity
        fields = ["name", "amount"]
