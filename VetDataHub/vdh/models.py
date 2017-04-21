from __future__ import unicode_literals

from django.db import models
from PIL import ImageFile


PROGRAM_CHOICES= (('CERT' , 'Certificate in AH'),('DIP' , 'Diploma in AH'),('BSC' , 'Bachelor of Science in AH'),('BVM' , 'Bachelor of Science in Vetenary Medicine'))


class Vet(models.Model):
	first_name= models.CharField(max_length=50)
	last_name= models.CharField(max_length=50)
	kvb_reg_no= models.IntegerField(unique=True, primary_key=True)
	email= models.EmailField()
	academic_inst= models.CharField(max_length=100)
	program_studied= models.CharField (max_length=100, choices= PROGRAM_CHOICES )
	index_no= models.IntegerField(unique=True)
	year_of_graduation= models.DateField(auto_now= False, auto_now_add=False)
	academic_cert_reg_no= models.IntegerField(unique=True)
	any_other_certs= models.CharField(max_length=500)
	license_no= models.IntegerField(unique=True)
	license_exp_date= models.DateField(auto_now= False, auto_now_add=False)
	current_station_of_work= models.CharField(max_length=100)

	def __str__(self):
		return '{0} {1}, KVB Reg No: {2}'.format(self.first_name, self.last_name, self.kvb_reg_no)

class Practitioner(models.Model):
	first_name= models.CharField(max_length=50)
	last_name= models.CharField(max_length=50)
	kvb_reg_no= models.IntegerField(unique=True, primary_key=True)
	email= models.EmailField()
	academic_inst= models.CharField(max_length=100)
	program_studied= models.CharField (max_length=100, choices= PROGRAM_CHOICES )
	index_no= models.IntegerField(unique=True)
	year_of_graduation= models.DateField(auto_now= False, auto_now_add=False)
	academic_cert_reg_no= models.IntegerField(unique=True)
	any_other_certs= models.CharField(max_length=500)
	license_no= models.IntegerField(unique=True)
	license_exp_date= models.DateField(auto_now= False, auto_now_add=False)
	current_station_of_work= models.CharField(max_length=100)
	is_vpp= models.BooleanField(default=False)
	supervising_vet= models.ForeignKey(Vet, models.DO_NOTHING, default=0)


	def __str__(self):
		return '{0} {1}, KVB Reg No: {2}'.format(self.first_name, self.last_name, self.kvb_reg_no)
