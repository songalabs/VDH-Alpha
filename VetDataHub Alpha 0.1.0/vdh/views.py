from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import ListView, DetailView, View
from .models import *
from django.contrib.auth import login, authenticate


from .forms import *



def dashboard(request):
	return render(request, 'vdh/admin-pages/dashboard.html')

def vpp_edit_profile(request):
	if request.method == 'POST':
		epp_form = EditVppProfileForm(request.POST)
		
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
#
#TODO: create at least 1 Vet instance before filling field below
#

			supervising_vet= epp_form.cleaned_data['supervising_vet']
	
			new_vpp = epp_form.save()
	
			return HttpResponseRedirect('/edit-profile/success/')

	else:
		epp_form= EditVppProfileForm()

	return render(request, 'vdh/forms/vpp-profile-form.html',{'epp_form': epp_form})



def vet_edit_profile(request):
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

	return render(request, 'vdh/forms/vet-profile-form.html',{'evp_form': evp_form})



def med_distributer_edit_profile(request):
	if request.method == 'POST':
		vmd_form = EditVetMedDistributerProfileForm(request.POST)
		
		if vmd_form.is_valid():
			#profile_picture = vmd_form.cleaned_data['profile_picture']
			first_name= vmd_form.cleaned_data['first_name']
			last_name= vmd_form.cleaned_data['last_name']
			kvb_reg_no= vmd_form.cleaned_data['kvb_reg_no']
			email= vmd_form.cleaned_data['email']
			academic_inst= vmd_form.cleaned_data['academic_inst']
			program_studied= vmd_form.cleaned_data['program_studied']
			index_no= vmd_form.cleaned_data['index_no']
			year_of_graduation= vmd_form.cleaned_data['year_of_graduation']
			academic_cert_reg_no= vmd_form.cleaned_data['academic_cert_reg_no']
			any_other_certs= vmd_form.cleaned_data['any_other_certs']
			license_no= vmd_form.cleaned_data['license_no']
			license_exp_date= vmd_form.cleaned_data['license_exp_date']
			current_station_of_work= vmd_form.cleaned_data['current_station_of_work']
	
			new_med_d = vmd_form.save()
	
			return HttpResponseRedirect('/edit-profile/success/')

	else:
		vmd_form= EditVetMedDistributerProfileForm()

	return render(request, 'vdh/forms/med-distributer-signup-form.html',{'vmd_form': vmd_form})

def med_producer_edit_profile(request):
	if request.method == 'POST':
		vmp_form = EditVetMedicineProducerProfileForm(request.POST)
		
		if vmp_form.is_valid():
			#profile_picture = vmp_form.cleaned_data['profile_picture']
			first_name= vmp_form.cleaned_data['first_name']
			last_name= vmp_form.cleaned_data['last_name']
			kvb_reg_no= vmp_form.cleaned_data['kvb_reg_no']
			email= vmp_form.cleaned_data['email']
			academic_inst= vmp_form.cleaned_data['academic_inst']
			program_studied= vmp_form.cleaned_data['program_studied']
			index_no= vmp_form.cleaned_data['index_no']
			year_of_graduation= vmp_form.cleaned_data['year_of_graduation']
			academic_cert_reg_no= vmp_form.cleaned_data['academic_cert_reg_no']
			any_other_certs= vmp_form.cleaned_data['any_other_certs']
			license_no= vmp_form.cleaned_data['license_no']
			license_exp_date= vmp_form.cleaned_data['license_exp_date']
			current_station_of_work= vmp_form.cleaned_data['current_station_of_work']
	
			new_med_p = vmp_form.save()
	
			return HttpResponseRedirect('/edit-profile/success/')

	else:
		vmp_form= EditVetMedicineProducerProfileForm()

	return render(request, 'vdh/forms/med-producer-signup-form.html',{'vmp_form': vmp_form})



def med_producer_data(request):
	if request.method == 'POST':
		med_prod_data_form = VetMedicineProductionDataForm(request.POST)
		
		if med_prod_data_form.is_valid():
			user = med_prod_data_form.cleaned_data['user']
			entry_no = med_prod_data_form.cleaned_data['entry_no']
			date = med_prod_data_form.cleaned_data['date']
			product_name = med_prod_data_form.cleaned_data['product_name']
			opening_balance = med_prod_data_form.cleaned_data['opening_balance']
			produced_quantity = med_prod_data_form.cleaned_data['produced_quantity']
			produced_batch_no =  med_prod_data_form.cleaned_data['produced_batch_no']
			distributed_quantity = med_prod_data_form.cleaned_data['distributed_qunatity']
			distributed_batch_no =  med_prod_data_form.cleaned_data['distributed_batch_no']
			distributed_to = med_prod_data_form.cleaned_data['distributed_to']
			
			new_med_p = med_prod_data_form.save()
	
			return HttpResponseRedirect('/data-entry/success/')

	else:
		med_prod_data_form= VetMedicineProductionDataForm()

	return render(request, 'vdh/forms/med-producer-data-form.html',{'med_prod_data_form': med_prod_data_form})

def med_distributer_data(request):
	if request.method == 'POST':
		med_dist_data_form = VetMedicineDistributionDataForm(request.POST)
		
		if med_dist_data_form.is_valid():
			user = med_dist_data_form.cleaned_data['user']
			entry_no = med_dist_data_form.cleaned_data['entry_no']
			date = med_dist_data_form.cleaned_data['date']
			product_name = med_dist_data_form.cleaned_data['product_name']
			opening_balance = med_dist_data_form.cleaned_data['opening_balance']
			procured_quantity = med_dist_data_form.cleaned_data['procured_quantity']
			procured_batch_no =  med_dist_data_form.cleaned_data['procured_batch_no']
			procured_from =  med_dist_data_form.cleaned_data['procured_from']
			distributed_quantity = med_dist_data_form.cleaned_data['distributed_qunatity']
			distributed_batch_no =  med_dist_data_form.cleaned_data['distributed_batch_no']
			distributed_to = med_dist_data_form.cleaned_data['distributed_to']
			
			new_med_p = med_dist_data_form.save()
	
			return HttpResponseRedirect('/data-entry/success/')

	else:
		med_dist_data_form= VetMedicineDistributionDataForm()

	return render(request, 'vdh/forms/med-distributer-data-form.html',{'med_dist_data_form': med_dist_data_form})

def clinical_work_data(request):
	if request.method == 'POST':
		clinical_work_data_form = ClinicalWorkDataForm(request.POST)
		
		if clinical_work_data_form.is_valid():
			user = clinical_work_data_form.cleaned_data['user']
			date = clinical_work_data_form.cleaned_data['date']
			animal_species = clinical_work_data_form.cleaned_data['animal_species']
			identification = clinical_work_data_form.cleaned_data['identification']
			owner = clinical_work_data_form.cleaned_data['owner']
			complaint = clinical_work_data_form.cleaned_data['complaint']
			diagnosis = clinical_work_data_form.cleaned_data['diagnosis']
			diagnostic_method_used = clinical_work_data_form.cleaned_data['diagnostic_method_used']
			treatment_product_used = clinical_work_data_form.cleaned_data['treatment_product_used']
			treatment_amount_used = clinical_work_data_form.cleaned_data['treatment_amount_used']
			treatment_batch_no =  clinical_work_data_form.cleaned_data['treatment_batch_no']
			outcome_of_treatment = clinical_work_data_form.cleaned_data['outcome_of_treatment']
			advice_given = clinical_work_data_form.cleaned_data['advice_given']
			
			new_med_p = clinical_work_data_form.save()
	
			return HttpResponseRedirect('/data-entry/success/')

	else:
		clinical_work_data_form= ClinicalWorkDataForm()

	return render(request, 'vdh/forms/clinical-work-data-form.html',{'clinical_work_data_form': clinical_work_data_form})
