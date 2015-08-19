#!/usr/bin/env python
import csv
import os
import sys

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

from main.models import Origin, Car, Car_Info

csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)) , "cars.csv")


csv_file = open(csv_file_path, 'rU')

reader = csv.DictReader(csv_file)
# print reader.fieldnames


for row in reader:
	print row
	origin_obj, created = Origin.objects.get_or_create(name=row['Origin'])
	origin_obj.save()

	car_obj, created = Car.objects.get_or_create(name=row['Car'])
	car_obj.year = row['Model']
	car_obj.origin = origin_obj
	car_obj.save()

	info_obj, created = Car_Info.objects.get_or_create(car=car_obj)
	info_obj.consump = row['MPG']
	info_obj.cylinders = row['Cylinders']
	info_obj.disp = row['Displacement']
	info_obj.bhp = row['Horsepower']
	info_obj.weight = row['Weight']
	info_obj.accel = row['Acceleration']
	try:
		info_obj.save()
	except Exception, e:
		print e
    	print row['Car']



