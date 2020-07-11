from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
# Create your views here.

def adminloginview(request):
	return render(request,'adminlogin.html', {})


def authenticateadmin(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username = username, password=password)

	if user is not None:
		login(request,user)
		return redirect('adminhomepage')

	if user is None:
		return redirect('adminloginpage')

def adminhomepageview(request):
	return render(request,'adminhomepage.html')
