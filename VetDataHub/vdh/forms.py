from django.forms import ModelForm
from .models import Practitioner, Vet
from django.utils.translation import ugettext_lazy as _


class EditPractitionerProfileForm(ModelForm):
	class Meta:
		model = Practitioner

		fields= [
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
			'is_vpp',
			
#
#TODO:after creating first vet instance; delete ']' above and place after uncommented code below.
#
			'supervising_vet',]
			

		labels= {
			'first_name':_('First name '),
			'last_name':_('Last name '),
			'kvb_reg_no':_('KVB Registration No '),
			'email':_('Email Address '),
			'academic_inst':_('Academic Institution '),
			'program_studied':_('Program Studied '),
			'index_no':_('Index No '),
			'year_of_graduation':_('Year of graduation '),
			'academic_cert_reg_no':_('Academic certificate No '),
			'any_other_certs':_('Any other certificates(seperate with comas) '),
			'license_no':_('License No '),
			'license_exp_date':_('License expiry date '),
			'current_station_of_work':_('Current station of work '),
			'is_vpp':_('Are you a vetenary paraprofessional(vpp)? '),
			
#
#TODO:after creating first vet instance; delete '}' above and place after uncommented code below.
#
			'supervising_vet':_('Select supervising vet'),}

class EditVetProfileForm(ModelForm):
	class Meta:
		model = Vet

		fields= [
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
			'first_name':_('First name '),
			'last_name':_('Last name '),
			'kvb_reg_no':_('KVB Registration No '),
			'email':_('Email Address '),
			'academic_inst':_('Academic Institution '),
			'program_studied':_('Program Studied '),
			'index_no':_('Index No '),
			'year_of_graduation':_('Year of graduation '),
			'academic_cert_reg_no':_('Academic certificate No '),
			'any_other_certs':_('Any other certificates(seperate with comas) '),
			'license_no':_('License No '),
			'license_exp_date':_('License expiry date '),
			'current_station_of_work':_('Current station of work '),
			}
