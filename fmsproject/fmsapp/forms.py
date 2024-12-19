from django import forms
from .models import UserRegistration
import re

class DateInput(forms.DateInput):
    input_type = "date"

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = "__all__"  # cng: Includes all fields except default ones like id and registrationtime
        widgets = {"password": forms.PasswordInput()}  # cng: Ensures password input is masked

    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True)  # cng: Added confirm_password field for validation

    def clean_studentid(self):
        studentid = self.cleaned_data['studentid']
        if not re.match(r'^23b0[a-z0-9]{6}$', studentid.lower()):
            raise forms.ValidationError("Student ID must start with '23b0' and contain 6 alphanumeric characters.")
        if UserRegistration.objects.filter(studentid=studentid).exists():  # cng: Checks for duplicate student ID
            raise forms.ValidationError("This student ID is already present.")
        return studentid.lower()

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@svecw.edu.in'):
            raise forms.ValidationError("Email must end with '@svecw.edu.in'.")
        if UserRegistration.objects.filter(email=email).exists():  # cng: Checks for duplicate email
            raise forms.ValidationError("This email is already present.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if UserRegistration.objects.filter(phone=phone).exists():  # cng: Checks for duplicate phone number
            raise forms.ValidationError("This phone number is already present.")
        return phone

    def clean(self):  # cng: Added clean method for cross-field validation
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Password and Confirm Password do not match.")
        return cleaned_data
