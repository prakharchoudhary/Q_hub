from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label='username', max_length=30, widget = forms.TextInput(attrs={'placeholder': 'Username'}))
	password = forms.CharField(
		label='password', 
		widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
		)
	