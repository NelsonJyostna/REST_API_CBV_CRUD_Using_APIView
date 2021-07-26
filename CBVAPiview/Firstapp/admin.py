from django.contrib import admin
from .models import Employee


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id', 'emp_name', 'emp_sal', 'emp_address']

admin.site.register(Employee, EmployeeAdmin)    