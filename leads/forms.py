from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'আপনার নাম'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'আপনার ইমেল'}),
        }