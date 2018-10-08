from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=25)
    email = forms.EmailField(max_length=100)
    password = forms.PasswordInput()
