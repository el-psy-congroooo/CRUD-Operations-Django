from django import forms
from .models import PersonalInformation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class PersonalInformationForm(forms.ModelForm):
    """
    This form is for to store the personal information.
    """

    class Meta:
        model = PersonalInformation
        fields = ('name', 'email', 'std', 'roll', 'sub')
        labels = {'email': 'E-Mail', 'std': 'Class',
                  'roll': 'Roll No', 'sub': 'Subjects'}
        widgets = {
            'sub': forms.Textarea(attrs={'rows': 5, 'cols': 23}),
        }


class LogInForm(forms.Form):
    """
    This form is for the user login and authentication.
    """

    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class SignUpForm(UserCreationForm):
    """
    This form is for user registration.
    """
    password1 = forms.CharField(label='Enter password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email", 'first_name', 'last_name', "password1", "password2")
        help_texts = {
            'username': None,
            'email': None,
            'password': None
        }
