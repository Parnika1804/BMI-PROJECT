from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Custom Mentor Registration Form (you can modify it based on your needs)
class MentorRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
