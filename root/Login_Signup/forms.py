from django import forms


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