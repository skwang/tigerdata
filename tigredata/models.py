from django.db import models
from jsonfield import JSONField

# Form storing all the JSON files
class Student(models.Model):
	netid = models.CharField(max_length=64)
	firstname = models.CharField(max_length=64)
	lastname = models.CharField(max_length=64)
	homecity = models.CharField(max_length=64)
	homecountry = models.CharField(max_length=64)
	degree = models.CharField(max_length=3)
	major = models.CharField(max_length=64)
	hall = models.CharField(max_length=64)
	room = models.CharField(max_length=64)
	rescollege = models.CharField(max_length=64)
	classyear = models.CharField(max_length=4)
	def __unicode__(self):
		return self.netid

class HallList(models.Model):
	halls = JSONField()
	def __unicode__(self):
		return "Hall List"
