from django.db import models


class stage(models.Model):
	'''
		Model for storing stage name
	'''
	stage_name = models.CharField(max_length=100)

	def __str__(self):
		return self.stage_name


class extraParam(models.Model):
	'''
		Model for storing extra parameter
	'''
	extra_param = models.CharField(max_length=100)
	
	def __str__(self):
		return self.extra_param


class singer(models.Model):
	'''
		Model for storing singer data
	'''
	name = models.CharField(max_length=100)
	date_of_birth = models.DateField()
	country_code = models.CharField(max_length=50)
	stage_name = models.ManyToManyField(stage)
	extra_param = models.ManyToManyField(extraParam)

	def __str__(self):
		return self.name
