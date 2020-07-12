from django.contrib import admin
from .models import PizzaModel, CustomerModel
# Register your models here.

admin.site.register(PizzaModel)
admin.site.register(CustomerModel)
