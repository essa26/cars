from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Origin(models.Model):
	name = models.CharField(max_length=255, unique=True)

	def __unicode__(self):
		return self.name



class Car(models.Model):
	name = models.CharField(max_length=255, unique=True)
	year = models.IntegerField(null=True)
	origin = models.ForeignKey('main.Origin', null=True)
	image = models.ImageField(upload_to="car", null=True)
 
	class Meta:
		ordering=['name'] # your select box will respect this as well.


	def __unicode__(self):
		return self.name

class Car_Info(models.Model):
	car = models.OneToOneField('main.Car')
	consump = models.FloatField(null=True) 
	cylinders = models.IntegerField(null=True) 
	disp = models.FloatField(null=True) 
	bhp = models.FloatField(null=True) 
	weight = models.FloatField(null=True) 
	accel = models.FloatField(null=True) 

	def __unicode__(self):
		return self.car.name


	def car_stats(self):
		value_list = []
		value_list.append("MPG: %s" % self.consump) 
		value_list.append("Number of Cylinders: %s" % self.cylinders)
		value_list.append("Displacement: %s " % self.disp)
		value_list.append("Power: %s horsepower" % self.bhp)
		value_list.append("Weight: %s " % self.weight)
		value_list.append("Acceleration (0-60): %s " % self.accel)
		return value_list


class Review(models.Model):
	author = models.ForeignKey(User)
	date_created = models.DateTimeField(auto_now=True)
	car_review = models.TextField()
	car = models.ForeignKey('main.Car')

	def __unicode__(self):
		return self.car_review





