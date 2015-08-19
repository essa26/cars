from django.contrib import admin

from main.models import Origin, Car, Car_Info, Review
# Register your models here.

admin.site.register(Origin)
admin.site.register(Car)
admin.site.register(Car_Info)
admin.site.register(Review)