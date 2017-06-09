from registration.forms import RegistrationForm


from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class RegForm(UserCreationForm):

	password = forms.CharField(widget = forms.PasswordInput)

	class Meta:
		model = User

		fields= [
			'username',
			'password1',
			'password2',
			'email',
			'first_name',
			'last_name' ,
			]

		labels= {
			'username':_('Username'),
			'password1':_('Password'),
			'password2':_('Password Again'),
			'email':_('Email Address '),
			'first_name':_('First name '),
			'last_name':_('Last name '),
			}

