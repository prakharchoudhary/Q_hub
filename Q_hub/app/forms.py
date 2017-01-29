from models import Filter, QuestionDetail
from django import forms
from ckeditor.widgets import CKEditorWidget

class LoginForm(forms.Form):

	username = forms.CharField(
								label='username', 
								max_length=30, 
								widget = forms.TextInput(attrs={'placeholder': 'Username', 'name': 'fname'})
							)
	password = forms.CharField(
		label='password', 
		widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'name': 'pword'})
		)
	

class FilterForm(forms.ModelForm):

	class Meta:
		model = Filter
		fields = ('branch', 'year', 'subject')

class QuestionForm(forms.ModelForm):

	class Meta:
		model = QuestionDetail
		exclude = ('owner','date_created', 'n_used', 'imp', 'subject', 'branch')
		widgets = {'description': CKEditorWidget, }