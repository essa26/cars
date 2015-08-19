from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from main.models import Origin, Car, Car_Info, Review, User
from django.template import RequestContext
from main.forms import CarSearch, CreateReview, UserSignUp, UserLogin, CreateCar
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

# Create your views here.

def home(request):

	context = {}

	origins = Origin.objects.all()

	context['origins'] = origins

	return render_to_response('home.html', context, context_instance=RequestContext(request))


#getting the car information using pk
def car_detail(request, pk):

	context = {}

	origins = Origin.objects.all()

	context['origins'] = origins

	car = Car.objects.get(pk=pk)

	context ['car'] = car

	form = CreateReview(initial={'car':car.pk,'car_review':""})

	context['form'] = form

	if request.method == 'POST':
		form = CreateReview(request.POST)
		if request.user.is_authenticated():
			if form.is_valid():
				author = request.user
				car_review = form.cleaned_data['car_review']
				
				new_review = Review.objects.get_or_create(author=author, car_review=car_review, car=car)
				context['valid'] = "Review Saved"
			

	return render_to_response('car_detail.html', context, context_instance=RequestContext(request))

def form_view(request):

	context = {}

	origins = Origin.objects.all()

	

	context['origins'] = origins
	

	get = request.GET
	post = request.POST

	context['get'] = get
	context['post'] = post


	if request.method == "POST":
		car = request.POST.get('car', None)

		cars = Car.objects.filter(name__icontains=car)

		context['cars'] = cars

	elif request.method == "GET":
		context['method'] = 'The method was GET'



	return render_to_response('form_view.html', context, context_instance=RequestContext(request))




#view listing cars
def car_list_template(request):

	origins = Origin.objects.all()

	context = {}

	context['origins'] = origins


	return render(request, 'car_list.html', context)

def origin_list_template(request, origin):

	origins = Origin.objects.all()

	area = Origin.objects.get(name=origin)

	context = {}

	context['area'] = area
	context['origins'] = origins


	return render(request, 'origin_list.html', context)



#html-less views
def car_list_view(request):

	origins = Origin.objects.all()

	car_string = ""

	for origin in origins:


		car_string += "<h4>%s</h4> " % origin

		for car in origin.car_set.all():
			car_string += "%s</br>" % car.name

		print origin.car_set.all()

	return HttpResponse(car_string)


def car_search(request, car):

	cars = Car.objects.filter(name__icontains=car)

	car_string = ""

	for car in cars:
		car_string += "<b>Car:</b>%s, <b>Origin:</b>%s </br>" % (car.name, car.origin)

	return HttpResponse(car_string)


def get_car_search(request):
	
	#cereal = request.GET['cereal']

	car = request.GET.get('car', 'None')

	cars = Car.objects.filter(name__icontains=car)
	
	print cars

	car_string = """
	<form action='/get_car_search/' method='GET'>

	Car:
	</br>
	<input type="text" name="car" >
	</br>
	</br>
	<input type="submit" value="Submit">

	</form>


	"""
	for car in cars:
		car_string += "<b>Car:</b>%s, <b>Origin:</b>%s </br>" % (car.name, car.origin)

	return HttpResponse(car_string)

def signup(request):

	context = {}

	origins = Origin.objects.all()

	

	context['origins'] = origins

	form = UserSignUp()
	context['form'] = form 

	if request.method == 'POST':
		form = UserSignUp(request.POST)
		if form.is_valid():

			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']

			try:
				new_user = User.objects.create_user(name, email, password)
				context['valid'] = "Thank you for signing up!"

				auth_user = authenticate(username=name, password=password)
				login(request, auth_user)
				return HttpResponseRedirect('/car_list_template')


			except IntegrityError, e:
				context['valid'] = "A user with that name already exists!"
		else:
			context['valid'] = form.errors

	if request.method == 'GET':
		context['valid'] = "Please sign up!"



	return render_to_response('signup.html', context, context_instance=RequestContext(request))


def login_view(request):

	redirect_to = request.REQUEST.get('next', '')

	context = {}

	origins = Origin.objects.all()

	

	context['origins'] = origins

	context['form'] = UserLogin()

	username = request.POST.get('username', None)
	password = request.POST.get('password', None)

	auth_user = authenticate(username=username, password=password)

	if auth_user is not None:
		if auth_user.is_active:
			login(request, auth_user)
			context['valid'] = "Login Successful"

			return HttpResponseRedirect(redirect_to)
		else:
			context['valid'] = "Invalid User"
	else:
		context['valid'] = "Please enter a User"
		
	return render_to_response('login.html', context, context_instance=RequestContext(request))


def logout_view(request):

	redirect_to = request.REQUEST.get('next', '')
	print redirect_to

	logout(request)

	return HttpResponseRedirect(redirect_to)

def add_review(request):
	context = {}

	origins = Origin.objects.all()

	

	context['origins'] = origins

	form = CreateReview()
	context['form'] = form 
	if request.method == 'POST':
		form = CreateCReview(request.POST)

		if form.is_valid():
			form.save()

			context['valid'] = "Review Saved"

	elif request.method == 'GET':
		context['valid'] = form.errors
	return render_to_response('add_review.html', context, context_instance=RequestContext (request))

def car_create(request):

	context = {}

	origins = Origin.objects.all()

	

	context['origins'] = origins

	form = CreateCar()
	context['form'] = form

	if request.method == 'POST':
		form = CreateCar(request.POST)

		if form.is_valid():
			form.save()

			context['valid'] = "Car Saved"

	elif request.method == 'GET':
		context['valid'] = form.errors
	return render_to_response('car_create.html', context, context_instance=RequestContext (request))

def about(request):

	context = {}

	origins = Origin.objects.all()

	

	context['origins'] = origins

	return render_to_response('about.html', context, context_instance=RequestContext (request))

def contact(request):

	context = {}

	origins = Origin.objects.all()

	

	context['origins'] = origins

	return render_to_response('contact.html', context, context_instance=RequestContext (request))





