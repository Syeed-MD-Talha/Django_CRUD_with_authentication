from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class LoginForm(forms.Form):
    username=forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'id':'loginUsername',
                'placeholder':'Username'
            }
        )
        )
    password=forms.CharField(
        max_length=65,
        widget=forms.PasswordInput(
            attrs={
                'id':'loginPassword',
                 'placeholder':'Password'
            }
        )
    )




class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        