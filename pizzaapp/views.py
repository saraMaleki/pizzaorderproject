from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
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
	return render(request,'adminhomepage.html')


def logoutadmin(request):
	logout(request)
	return redirect('adminloginpage')