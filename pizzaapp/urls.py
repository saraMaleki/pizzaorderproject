from django.contrib import admin
from django.urls import path
from .views import adminloginview, adminhomepageview,authenticateadmin


urlpatterns = [
	path('admin/', adminloginview, name='adminloginpage'),
	path('adminauthenticate/', authenticateadmin, name='authenticateadmin'),
	path('admin/homepage/', adminhomepageview, name='adminhomepage')

]