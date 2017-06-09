from django.forms import ModelForm
from .models import *
from django import forms
from django.utils.translation import ugettext_lazy as _


class EditVppProfileForm(ModelForm):
	class Meta:
		model = VppProfile

		fields= [
			'user',
			'first_name',
			'last_name' ,
			'kvb_reg_no',
			'email' ,
			'academic_inst',
			'program_studied',
			'index_no',
			'year_of_graduation',
			'academic_cert_reg_no',
			'any_other_certs',
			'license_no',
			'license_exp_date',
			'current_station_of_work',
			
#
#TODO:after creating first vet instance; delete ']' above and place after uncommented code below.
#
			'supervising_vet',]
			

		labels= {
			'user':_('User '),
			'first_name':_('First name '),
			'last_name':_('Last name '),
			'kvb_reg_no':_('KVB Registration No '),
			'email':_('Email Address '),
			'academic_inst':_('Academic Institution '),
			'program_studied':_('Program Studied '),
			'index_no':_('Index No '),
			'year_of_graduation':_('Date of graduation '),
			'academic_cert_reg_no':_('Academic certificate No '),
			'any_other_certs':_('Any other certificates(seperate with comas) '),
			'license_no':_('License No '),
			'license_exp_date':_('License expiry date '),
			'current_station_of_work':_('Current station of work '),
			
#
#TODO:after creating first vet instance; delete '}' above and place after uncommented code below.
#
			'supervising_vet':_('Select supervising vet'),}

class EditVetProfileForm(ModelForm):
	class Meta:
		model = VetProfile

		fields= [
			'user',
			'first_name',
			'last_name' ,
			'kvb_reg_no',
			'email' ,
			'academic_inst',
			'program_studied',
			'index_no',
			'year_of_graduation',
			'academic_cert_reg_no',
			'any_other_certs',
			'license_no',
			'license_exp_date',
			'current_station_of_work',
			]


		labels= {
			'user':_('User '),
			'first_name':_('First name '),
			'last_name':_('Last name '),
			'kvb_reg_no':_('KVB Registration No '),
			'email':_('Email Address '),
			'academic_inst':_('Academic Institution '),
			'program_studied':_('Program Studied '),
			'index_no':_('Index No '),
			'year_of_graduation':_('Date of graduation '),
			'academic_cert_reg_no':_('Academic certificate No '),
			'any_other_certs':_('Any other certificates(seperate with comas) '),
			'license_no':_('License No '),
			'license_exp_date':_('License expiry date '),
			'current_station_of_work':_('Current station of work '),
			}

class EditVetMedicineProducerProfileForm(ModelForm):
	class Meta:
		model = VetMedicineProducerProfile

		fields= [
			'user',
			'first_name',
			'last_name' ,
			'kvb_reg_no',
			'email' ,
			'academic_inst',
			'program_studied',
			'index_no',
			'year_of_graduation',
			'academic_cert_reg_no',
			'any_other_certs',
			'license_no',
			'license_exp_date',
			'current_station_of_work',
			]


		labels= {
			'user':_('User '),
			'first_name':_('First name '),
			'last_name':_('Last name '),
			'kvb_reg_no':_('KVB Registration No '),
			'email':_('Email Address '),
			'academic_inst':_('Academic Institution '),
			'program_studied':_('Program Studied '),
			'index_no':_('Index No '),
			'year_of_graduation':_('Date of graduation '),
			'academic_cert_reg_no':_('Academic certificate No '),
			'any_other_certs':_('Any other certificates(seperate with comas) '),
			'license_no':_('License No '),
			'license_exp_date':_('License expiry date '),
			'current_station_of_work':_('Current station of work '),
			}

class EditVetMedDistributerProfileForm(ModelForm):
	class Meta:
		model = VetMedicineProducerProfile

		fields= [
			'user',
			'first_name',
			'last_name' ,
			'kvb_reg_no',
			'email' ,
			'academic_inst',
			'program_studied',
			'index_no',
			'year_of_graduation',
			'academic_cert_reg_no',
			'any_other_certs',
			'license_no',
			'license_exp_date',
			'current_station_of_work',
			]


		labels= {
			'user':_('User '),
			'first_name':_('First name '),
			'last_name':_('Last name '),
			'kvb_reg_no':_('KVB Registration No '),
			'email':_('Email Address '),
			'academic_inst':_('Academic Institution '),
			'program_studied':_('Program Studied '),
			'index_no':_('Index No '),
			'year_of_graduation':_('Date of graduation '),
			'academic_cert_reg_no':_('Academic certificate No '),
			'any_other_certs':_('Any other certificates(seperate with comas) '),
			'license_no':_('License No '),
			'license_exp_date':_('License expiry date '),
			'current_station_of_work':_('Current station of work '),
			}

class ClinicalWorkDataForm(ModelForm):
	class Meta:
		model = ClinicalWorkData

		fields= [
			'animal_species',
			'identification',
			'owner',
			'complaint',
			'diagnosis',
			'diagnostic_method_used',
			'treatment_product_used',
			'treatment_amount_used',
			'treatment_batch_no',
			'outcome_of_treatment',
			'advice_given',
			]


		labels= {
			'animal_species':_('Animal Species'),
			'identification':_('Identification'),
			'owner':_('Owner'),
			'complaint':_('Complaint'),
			'diagnosis':_('Diagnosis'),
			'diagnostic_method_used':_('Diagnostic method used'),
			'treatment_product_used':_('Treatment product given'),
			'treatment_amount_used':_('Treatment amount used'),
			'treatment_batch_no':_('Treatment batch no'),
			'outcome_of_treatment':_('Outcome of treatment'),
			'advice_given':_('Advice given'),
			}

class VetMedicineProductionDataForm(ModelForm):
	class Meta:
		model = VetMedicineProductionData

		fields= [
			'entry_no',
			'date',
			'product_name',
			'opening_balance',
			'produced_quantity',
			'produced_batch_no',
			'distributed_quantity',
			'distributed_batch_no',
			'distributed_to',
			'balance_in_stock',
			]


		labels= {
			'entry_no':_('Entry No'),
			'date':_('Date'),
			'product_name':_('Product name'),
			'opening_balance':_('Opening balance'),
			'produced_quantity':_('Produced quantity'),
			'produced_batch_no':_('Produced batch no'),
			'distributed_quantity':_('Distributed quantity'),
			'distributed_batch_no':_('Distributed batch no'),
			'distributed_to':_('Distributed to'),
			'balance_in_stock':_('Balance in stock'),
			}

class VetMedicineDistributionDataForm(ModelForm):
	class Meta:
		model = VetMedicineDistributionData

		fields= [
			'entry_no',
			'date',
			'product_name',
			'opening_balance',
			'procured_quantity',
			'procured_batch_no',
			'procured_from',
			'distributed_quantity',
			'distributed_batch_no',
			'distributed_to',
			'balance_in_stock',
			]


		labels= {
			'entry_no':_('Entry No'),
			'date':_('Date'),
			'product_name':_('Product name'),
			'opening_balance':_('Opening balance'),
			'procured_quantity':_('Procured quantity'),
			'procured_batch_no':_('Procured batch no'),
			'procured_from':_('Procured from'),
			'distributed_quantity':_('Distributed quantity'),
			'distributed_batch_no':_('Distributed batch no'),
			'distributed_to':_('Distributed to'),
			'balance_in_stock':_('Balance in stock'),
			}
