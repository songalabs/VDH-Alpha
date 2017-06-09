from __future__ import unicode_literals

from django.db import models
from PIL import ImageFile
from django.contrib.auth.models import User
from .middleware import *

PROGRAM_CHOICES= (('CERT' , 'Certificate in AH'),('DIP' , 'Diploma in AH'),('BSC' , 'Bachelor of Science in AH'),('BVM' , 'Bachelor of Science in Vetenary Medicine'))
USER = get_current_user()
# USER MODELS

class VetProfile(models.Model):
	user = models.ForeignKey(User)
	first_name= models.CharField(max_length=50)
	last_name= models.CharField(max_length=50)
	kvb_reg_no= models.IntegerField(unique=True, primary_key=True)
	email= models.EmailField()
	academic_inst= models.CharField(max_length=100)
	program_studied= models.CharField (max_length=100, choices= PROGRAM_CHOICES )
	index_no= models.IntegerField(unique=True)
	year_of_graduation= models.DateField(auto_now= False, auto_now_add=False, help_text= "Please use the following format: <em>MM-DD-YYYY</em>.")
	academic_cert_reg_no= models.IntegerField(unique=True)
	any_other_certs= models.CharField(max_length=500, blank=True)
	license_no= models.IntegerField(unique=True)
	license_exp_date= models.DateField(auto_now= False, auto_now_add=False, help_text= "Please use the following format: <em>MM-DD-YYYY</em>.")
	current_station_of_work= models.CharField(max_length=100)

	def __str__(self):
		return '{0} {1}, KVB Reg No: {2}'.format(self.first_name, self.last_name, self.kvb_reg_no)

class VppProfile(models.Model):
	user = models.ForeignKey(User)
	first_name= models.CharField(max_length=50)
	last_name= models.CharField(max_length=50)
	kvb_reg_no= models.IntegerField(unique=True, primary_key=True)
	email= models.EmailField()
	academic_inst= models.CharField(max_length=100)
	program_studied= models.CharField (max_length=100, choices= PROGRAM_CHOICES )
	index_no= models.IntegerField(unique=True)
	year_of_graduation= models.DateField(auto_now= False, auto_now_add=False, help_text= "Please use the following format: <em>MM-DD-YYYY</em>.")
	academic_cert_reg_no= models.IntegerField(unique=True)
	any_other_certs= models.CharField(max_length=500, blank=True)
	license_no= models.IntegerField(unique=True)
	license_exp_date= models.DateField(auto_now= False, auto_now_add=False, help_text= "Please use the following format: <em>MM-DD-YYYY</em>.")
	current_station_of_work= models.CharField(max_length=100)
	supervising_vet= models.ForeignKey(VetProfile, models.DO_NOTHING, default=0)


	def __str__(self):
		return '{0} {1}, KVB Reg No: {2}'.format(self.first_name, self.last_name, self.kvb_reg_no)

class VetMedicineProducerProfile(models.Model):
	user = models.ForeignKey(User)
	first_name= models.CharField(max_length=50)
	last_name= models.CharField(max_length=50)
	kvb_reg_no= models.IntegerField(unique=True, primary_key=True)
	email= models.EmailField()
	academic_inst= models.CharField(max_length=100)
	program_studied= models.CharField (max_length=100, choices= PROGRAM_CHOICES )
	index_no= models.IntegerField(unique=True)
	year_of_graduation= models.DateField(auto_now= False, auto_now_add=False, help_text= "Please use the following format: <em>MM-DD-YYYY</em>.")
	academic_cert_reg_no= models.IntegerField(unique=True)
	any_other_certs= models.CharField(max_length=500, blank=True)
	license_no= models.IntegerField(unique=True)
	license_exp_date= models.DateField(auto_now= False, auto_now_add=False, help_text= "Please use the following format: <em>MM-DD-YYYY</em>.")
	current_station_of_work= models.CharField(max_length=100)

	def __str__(self):
		return '{0} {1}, KVB Reg No: {2}'.format(self.first_name, self.last_name, self.kvb_reg_no)

class VetMedicineDistributerProfile(models.Model):
	user = models.ForeignKey(User)
	first_name= models.CharField(max_length=50)
	last_name= models.CharField(max_length=50)
	kvb_reg_no= models.IntegerField(unique=True, primary_key=True)
	email= models.EmailField()
	academic_inst= models.CharField(max_length=100)
	program_studied= models.CharField (max_length=100, choices= PROGRAM_CHOICES )
	index_no= models.IntegerField(unique=True)
	year_of_graduation= models.DateField(auto_now= False, auto_now_add=False, help_text= "Please use the following format: <em>MM-DD-YYYY</em>.")
	academic_cert_reg_no= models.IntegerField(unique=True)
	any_other_certs= models.CharField(max_length=500, blank=True)
	license_no= models.IntegerField(unique=True)
	license_exp_date= models.DateField(auto_now= False, auto_now_add=False, help_text= "Please use the following format: <em>MM-DD-YYYY</em>.")
	current_station_of_work= models.CharField(max_length=100)

	def __str__(self):
		return '{0} {1}, KVB Reg No: {2}'.format(self.first_name, self.last_name, self.kvb_reg_no)



# DATA FORM MODELS

CATEGORY_CHOICES = (('CW','Clinical work/ Herd health/ Extension service'),('VMP','Vetenary medicine production'),('VMD','Vetenary medicine distribution')) 

DIAGNOSTIC_METHOS_USED_CHOICES = (('TENT','Tentative'),('LAB','Lab'),('SURG','Surgical'),('PHY','Physical exam eg, Palpation'))


class PracticeData(models.Model):
	category = models.CharField (max_length=100, choices= CATEGORY_CHOICES )

	def __str__(self):
		return category

class ClinicalWorkData(models.Model):
	user = models.ForeignKey(User, default= None)
	date = models.DateField(auto_now= False, auto_now_add=False, help_text= "Please use the following format: <em>MM-DD-YYYY</em>.")
	animal_species = models.CharField(max_length=100)
	identification = models.CharField(max_length=100)
	owner = models.CharField(max_length=100)
	complaint = models.CharField(max_length=1000)
	diagnosis = models.CharField(max_length=1000)
	diagnostic_method_used = models.CharField (max_length=100, choices= DIAGNOSTIC_METHOS_USED_CHOICES )
	treatment_product_used = models.CharField(max_length=100)
	treatment_amount_used = models.CharField(max_length=100)
	treatment_batch_no =  models.IntegerField(unique= True)
	outcome_of_treatment = models.CharField(max_length=500)
	advice_given = models.CharField(max_length=1000)

	def __str__(self):
		return ' Date: {0}, Diagnosis: {1}, Outcome of treatment: {2}'.format(self.date, self.diagnosis, self.outcome_of_treatment)

class VetMedicineProductionData(models.Model):
	user = models.ForeignKey(User, default= None)
	entry_no = models.AutoField(primary_key=True)
	date = models.DateField(auto_now= False, auto_now_add=False, help_text= "Please use the following format: <em>MM-DD-YYYY</em>.")
	product_name = models.CharField(max_length=100)
	opening_balance = models.IntegerField()
	produced_quantity = models.IntegerField()
	produced_batch_no =  models.IntegerField(unique= True)
	distributed_quantity = models.IntegerField()
	distributed_batch_no =  models.IntegerField(unique= True)
	distributed_to = models.ForeignKey(VetMedicineDistributerProfile, models.DO_NOTHING, default=0, null=True, blank= True)
	balance_in_stock = models.IntegerField()

	def __str__(self):
		return ' Date: {0}, Product: {1}, Quantity Produced: {2}, Quantity Distributed: {3} Distributed To: {4}'.format(self.date, self.product_name, self.produced_quantity, self.distributed_quantity, self.distributed_to)

class VetMedicineDistributionData(models.Model):
	user = models.ForeignKey(User, default= None)
	entry_no = models.AutoField(primary_key=True)
	date = models.DateField(auto_now= False, auto_now_add=False, help_text= "Please use the following format: <em>MM-DD-YYYY</em>.")
	product_name = models.CharField(max_length=100)
	opening_balance = models.IntegerField()
	procured_quantity = models.IntegerField()
	procured_batch_no =  models.IntegerField(unique= True)
	procured_from =  models.ForeignKey(VetMedicineProducerProfile, models.DO_NOTHING, default=0, null=True, blank= True)
	distributed_quantity = models.IntegerField()
	distributed_batch_no =  models.IntegerField(unique= True)
	distributed_to = models.ForeignKey(VetProfile, models.DO_NOTHING, default=0, null=True, blank= True)
	balance_in_stock = models.IntegerField()

	def __str__(self):
		return ' Date: {0}, Data entry no: {1} Product: {2}, Quantity Procured: {3}, Procured from: {4} , Quantity distributed: {5}, Distributed To: {6}'.format(self.date, self.entry_no, self.product_name, self.procured_quantity, self.procured_from, self.distributed,_quantity, self.distributed_to)
