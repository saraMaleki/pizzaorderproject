from django.contrib import admin
from django.urls import path
from .views import adminloginview, adminhomepageview,authenticateadmin,logoutadmin,addpizza, deletepizza,homepageview, signupuser,userloginview, customerwelcomeview, userautenticate,userlogout, placeorder, userorders,adminorders,acceptorder,declineorder


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
	path('placeorder/', placeorder),
	path('userorders/',userorders, name='userorders'),
	path('adminorders/',adminorders, name='adminorders'),
	path('acceptorder/<int:orderpk>', acceptorder,name='acceptorder'),
	path('declineorder/<int:orderpk>', declineorder,name='declineorder'),
]