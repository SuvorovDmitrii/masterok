from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import *

admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Person)


# Register your models here.
