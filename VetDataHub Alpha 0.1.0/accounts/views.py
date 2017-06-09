from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

from accounts.forms import *

class UserFormView(View):
	form_class = RegForm
	template_name = 'registration/registration_form.html'

	def get(self, request):
		reg_form = self.form_class(None)
		return render(request, self.template_name, { reg_form : 'reg_form' })

	def self(self, request):
		reg_form = self.form_class(request.POST)

		if reg_form.is_valid():

			user= reg_form.save(commit=False)

			usename = reg_form.cleaned_data['username']
			password = reg_form.cleaned_data['password']
			email= reg_form.cleaned_data['email']
		
			user.set_password(password)
			user.save()


			user = authenticate(username=username, password=password)

			if user.is_active:
				login(request, user)
				return render('vdh:index')

		return render(request, self.template_name, { reg_form : 'reg_form' })
