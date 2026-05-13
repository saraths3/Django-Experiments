from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Employee, Teachers, MyStudents, userdata

admin.site.register(Employee)
admin.site.register(Teachers)
admin.site.register(MyStudents)
admin.site.register(userdata)