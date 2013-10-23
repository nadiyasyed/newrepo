from django import forms

class UserForm(forms.ModelForm):
    email = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)

