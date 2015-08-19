from django import forms 
from django.core.validators import RegexValidator
from main.models import Car, Review

letter_validator = RegexValidator(r'^[a-zA-Z]*$', 'Please Type Letters')
number_validator = RegexValidator(r'^[0-9]*$', 'Please Type Numbers')

class CarSearch(forms.Form):
	
	name = forms.CharField(required=True, validators=[letter_validator])#this is a field

class CreateReview(forms.ModelForm): #creates form from model created 

	class Meta:
		model = Review
		fields = ['car_review',]
		


class UserSignUp(forms.Form):
	name = forms.CharField(required=True, validators=[letter_validator])
	password = forms.CharField(widget=forms.PasswordInput(), required=True)
	email = forms.CharField(required=True)

class UserLogin(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True , widget=forms.PasswordInput())

class CreateCar(forms.ModelForm): #creates form from model created 
	class Meta:
		model = Car
		fields = '__all__'
