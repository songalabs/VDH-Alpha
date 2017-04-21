from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Vet, Practitioner

from .forms import EditPractitionerProfileForm, EditVetProfileForm



class VetList(ListView):
	model= Vet

class PractitionerList(ListView):
	model= Practitioner

class VetDetail(DetailView):
	queryset= Vet.objects.all()

class PractitionerDetail(DetailView):
	model= Practitioner

def user(request):
	return render(request, 'vdh/user.html')

def practitioner_form(request):
	if request.method == 'POST':
		epp_form = EditPractitionerProfileForm(request.POST)
		
		if epp_form.is_valid():
			#profile_picture = epp_form.cleaned_data['profile_picture']
			first_name= epp_form.cleaned_data['first_name']
			last_name= epp_form.cleaned_data['last_name']
			kvb_reg_no= epp_form.cleaned_data['kvb_reg_no']
			email= epp_form.cleaned_data['email']
			academic_inst= epp_form.cleaned_data['academic_inst']
			program_studied= epp_form.cleaned_data['program_studied']
			index_no= epp_form.cleaned_data['index_no']
			year_of_graduation= epp_form.cleaned_data['year_of_graduation']
			academic_cert_reg_no= epp_form.cleaned_data['academic_cert_reg_no']
			any_other_certs= epp_form.cleaned_data['any_other_certs']
			license_no= epp_form.cleaned_data['license_no']
			license_exp_date= epp_form.cleaned_data['license_exp_date']
			current_station_of_work= epp_form.cleaned_data['current_station_of_work']
			is_vpp= epp_form.cleaned_data['is_vpp']
#
#TODO: create at least 1 Vet instance before filling field below
#

			supervising_vet= epp_form.cleaned_data['supervising_vet']
	
			new_practitioner = epp_form.save()
	
			return HttpResponseRedirect('/edit-profile/success/')

	else:
		epp_form= EditPractitionerProfileForm()

	return render(request, 'vdh/practitioner-profile-form.html',{'epp_form': epp_form})

def vet_form(request):
	if request.method == 'POST':
		evp_form = EditVetProfileForm(request.POST)
		
		if evp_form.is_valid():
			#profile_picture = evp_form.cleaned_data['profile_picture']
			first_name= evp_form.cleaned_data['first_name']
			last_name= evp_form.cleaned_data['last_name']
			kvb_reg_no= evp_form.cleaned_data['kvb_reg_no']
			email= evp_form.cleaned_data['email']
			academic_inst= evp_form.cleaned_data['academic_inst']
			program_studied= evp_form.cleaned_data['program_studied']
			index_no= evp_form.cleaned_data['index_no']
			year_of_graduation= evp_form.cleaned_data['year_of_graduation']
			academic_cert_reg_no= evp_form.cleaned_data['academic_cert_reg_no']
			any_other_certs= evp_form.cleaned_data['any_other_certs']
			license_no= evp_form.cleaned_data['license_no']
			license_exp_date= evp_form.cleaned_data['license_exp_date']
			current_station_of_work= evp_form.cleaned_data['current_station_of_work']
	
			new_vet = evp_form.save()
	
			return HttpResponseRedirect('/edit-profile/success/')

	else:
		evp_form= EditVetProfileForm()

	return render(request, 'vdh/vet-profile-form.html',{'evp_form': evp_form})