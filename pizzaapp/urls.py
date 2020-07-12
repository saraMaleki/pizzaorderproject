from django.contrib import admin
from django.urls import path
from .views import adminloginview, adminhomepageview,authenticateadmin,logoutadmin,addpizza, deletepizza,homepageview, signupuser,userloginview, customerwelcomeview, userautenticate,userlogout


urlpatterns = [
	path('adminlogin/', adminloginview, name='adminloginpage'),
	path('adminauthenticate/', authenticateadmin, name='authenticateadmin'),
	path('admin/homepage/', adminhomepageview, name='adminhomepage'),
	path('adminlogout/', logoutadmin, name='logoutadmin'),
	path('addpizza/', addpizza),
	path('deletepizza/<int:pizzapk>',deletepizza, name='deletepizza'),
	path('', homepageview, name='homepage'),
	path('signupuser/', signupuser, name='signupuser'),
	path('loginuser/', userloginview, name='userloginpage'),
	path('customer/welcome',customerwelcomeview, name='customerpage'),
	path('customer/authenticate/', userautenticate, name='customerauthenticate'),
	path('userlogout/',userlogout, name='userlogout'),

]