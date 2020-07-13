from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import PizzaModel, CustomerModel, OrderModel
# Create your views here.

def adminloginview(request):
	return render(request,'adminlogin.html', {})


def authenticateadmin(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username = username, password=password)

	if user is not None and user.username=='admin':
		login(request,user)
		return redirect('adminhomepage')

	if user is None:
		messages.add_message(request, messages.ERROR, "invalid credentials")
		return redirect('adminloginpage')

def adminhomepageview(request):
	context = {'pizzas' : PizzaModel.objects.all()}
	return render(request,'adminhomepage.html',context)


def logoutadmin(request):
	logout(request)
	return redirect('adminloginpage')

def addpizza(request):
	name = request.POST['name']
	price = request.POST['price']
	PizzaModel(name = name, price=price).save()
	return redirect('adminhomepage')

def deletepizza(request, pizzapk):
	PizzaModel.objects.filter(id = pizzapk).delete()
	return redirect('adminhomepage')

def homepageview(request):
	return render(request,'homepage.html')

def signupuser(request):
	username = request.POST['username']
	password = request.POST['password']
	phoneno = request.POST['phoneno']

	if User.objects.filter(username = username).exists():
		messages.add_message(request,messages.ERROR, "user already exists")
		return redirect('homepage')

	User.objects.create_user(username = username, password = password).save()
	lastobject = len(User.objects.all())-1
	CustomerModel(userid = User.objects.all()[int(lastobject)].id, phoneno = phoneno).save()
	messages.add_message(request, messages.ERROR,"user successfully created")
	return redirect('homepage')

def userloginview(request):
	return render (request,'userlogin.html')

def userautenticate(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username = username, password=password)

	if user is not None:
		login(request,user)
		return redirect('customerpage')

	if user is None:
		messages.add_message(request, messages.ERROR, "invalid credentials")
		return redirect('userloginpage')

def customerwelcomeview(request):
	if not request.user.is_authenticated:
		return redirect('userloginpage')

	username = request.user.username
	context = {'username':username, 'pizzas':PizzaModel.objects.all()}
	return render(request,'customerwelcome.html',context)

def userlogout(request):
	logout(request)
	return redirect('userloginpage')


def placeorder(request):
	if not request.user.is_authenticated:
		return redirect('userloginpage')

	username = request.user.username
	phoneno = CustomerModel.objects.filter(userid = request.user.id)[0].phoneno
	address = request.POST['address']
	ordereditems =""
	for pizza in PizzaModel.objects.all():
		pizzaid = pizza.id
		print(pizzaid)
		name = pizza.name
		price = pizza.price
		quantity = request.POST.get(str(pizzaid)," ")
		print('qu '+ quantity)
		if str(quantity) !="0" and str(quantity) != " ":
			ordereditems = ordereditems + " " + name + " price: " + str(int(price)*int(quantity)) + " quantity: "+quantity
		print(ordereditems)
	OrderModel(username=username, phoneno=phoneno, address=address, ordereditems=ordereditems).save()
	messages.add_message(request,messages.SUCCESS,"order successfully placed")
	return redirect('customerpage')


def userorders(request):
	orders = OrderModel.objects.filter(username=request.user.username)
	context={'orders':orders}
	return render(request, 'userorders.html',context)

def adminorders(request):
	orders = OrderModel.objects.all()
	context = { 'orders': orders }
	return render(request, 'adminorders.html' ,context)

def acceptorder(request, orderpk):

	order =OrderModel.objects.filter(id=orderpk)[0]
	order.status="accepted"
	order.save()
	return redirect(request.META['HTTP_REFERER'])

def declineorder(request, orderpk):

	order =OrderModel.objects.filter(id=orderpk)[0]
	order.status="declied"
	order.save()
	return redirect(request.META['HTTP_REFERER'])

