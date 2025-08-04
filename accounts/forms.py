from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . import models
from phonenumber_field.formfields import PhoneNumberField



class RegisterionForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)
    email = forms.EmailField(required=True, label="Email address")
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'Enter first name',
            'last_name': 'Enter last name',
            'username': 'Enter username',
            'email': 'Enter email address',
            'password1': 'Enter password',
            'password2': 'Confirm Password',
        }
        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control mb-0',
                'placeholder': placeholders.get(name, '')
            })

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
                'username': 'Enter username',
                'email': 'Enter your email address',
                'password': 'Enter password',
            }
        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control mb-0',
                'placeholder': placeholders.get(name, '')
            })


class ProfileForm(forms.ModelForm):
    phone_number = PhoneNumberField(required=False)
    class Meta():
        model = models.Profile
        fields = ['phone_number', 'profile_photo', 'address']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control',
                'type': 'tel',
                'id': 'id_phone_number',
            }),
            'profile_photo': forms.FileInput(attrs={'class': 'file-upload','accept': 'image/*'}), 
            'address': forms.TextInput(attrs={'class': 'form-control'}), 
        }

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'username': forms.TextInput(attrs={'class': 'form-control'}), 
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


        