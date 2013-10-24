__author__ = 'nadiya'

from django import forms
from utils import ROLE_CHOICES


class LoginForm(forms.Form):
    email  = forms.EmailField(label='',
                    widget=forms.TextInput(
                        attrs={'placeholder': 'Email',
                               'class':'input-large ',
                               'style':'width:290px',
                               'id':'email',
                               'onfocus':"this.placeholder = ''",
                               'onblur':"this.placeholder = 'Email'"}
                    ))
    password  = forms.CharField(
            label='', widget=forms.PasswordInput(
                attrs={'placeholder':'password',
                       'class':'input-large ',
                       'style':'width:290px',
                       'id':'password',
                       'onfocus':"this.placeholder = ''",
                       'onblur':"this.placeholder = 'password'"}
            ))

class SignupForm(forms.Form):
    firstname = forms.CharField( label= '',widget=forms.PasswordInput(attrs={'placeholder':'firstname','class':'input-large ',
                       'style':'width:290px',
                       'id':'password',
                       'onfocus':"this.placeholder = ''",
                       'onblur':"this.placeholder = 'firstname'"}))

    lastname = forms.CharField( label= '',widget=forms.PasswordInput(attrs={'placeholder':'lastname','class':'input-large ',
                       'style':'width:290px',
                       'id':'password',
                       'onfocus':"this.placeholder = ''",
                       'onblur':"this.placeholder = 'lastname'"}))

    role        = forms.ChoiceField(
        widget = forms.Select(),
        choices = ROLE_CHOICES ,
        initial='user',
        required = True,)

    email  = forms.EmailField(label='',
                    widget=forms.TextInput(
                        attrs={'placeholder': 'Email',
                               'class':'input-large ',
                               'style':'width:290px',
                               'id':'email',
                               'onfocus':"this.placeholder = ''",
                               'onblur':"this.placeholder = 'Email'"}
                    ))
    password  = forms.CharField(
            label='', widget=forms.PasswordInput(
                attrs={'placeholder':'password',
                       'class':'input-large ',
                       'style':'width:290px',
                       'id':'password',
                       'onfocus':"this.placeholder = ''",
                       'onblur':"this.placeholder = 'password'"}
            ))

