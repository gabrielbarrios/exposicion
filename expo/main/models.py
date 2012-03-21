from django.db import models

class Student(models.Model):
	name = models.CharField(max_length=50)
	number = models.CharField(max_length=50) 
	
	def __unicode__(self):
		return "%s-%s" %(self.pk, self.name)

class Pet(models.Model):
	student = models.ForeignKey('student', related_name='pets')
	name = models.CharField(max_length=50)
	decription =  models.CharField(max_length=50)
