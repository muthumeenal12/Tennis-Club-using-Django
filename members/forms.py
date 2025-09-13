from django import forms
from .models import JoinRequest

class JoinRequestForm(forms.ModelForm):
    class Meta:
        model = JoinRequest
        fields = ['firstname', 'lastname', 'email', 'phone', 'message']
        widgets = {
            "message": forms.Textarea(attrs = {"rows":4}),
        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email or "@" not in email:
            raise forms.ValidationError("Please enter a valid email address.")
        return email
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone or not phone.isdigit() or len(phone) < 10:
            raise forms.ValidationError("Please enter a valid phone number.")
        return phone
    def clean_firstname(self):   
        firstname = self.cleaned_data.get('firstname')
        if not firstname or len(firstname) < 2:
            raise forms.ValidationError("First name must be at least 2 characters long.")
        return firstname    
    def clean_lastname(self):
        lastname = self.cleaned_data.get('lastname')
        if not lastname or len(lastname) < 2:
            raise forms.ValidationError("Last name must be at least 2 characters long.")
        return lastname