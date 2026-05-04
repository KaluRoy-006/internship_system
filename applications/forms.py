from django import forms
from .models import InternshipApplication

class InternshipApplicationForm(forms.ModelForm):
    class Meta:
        model = InternshipApplication
        exclude = ['applicant', 'status', 'date_applied']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'school_name': forms.TextInput(attrs={'class': 'form-control'}),
            'level_of_study': forms.Select(attrs={'class': 'form-select'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'internship_domain': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'cv': forms.FileInput(attrs={'class': 'form-control'}),
            'recommendation_letter': forms.FileInput(attrs={'class': 'form-control'}),
        }