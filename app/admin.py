from django.contrib import admin
from .models import (
    Student ,
    Company ,
    Domain ,
    Department ,
    Placement_Detail ,
)
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin) : 
    list_display = ['id' ,'name' , 'dept' , 'year_of_passing' ]
    readonly_fields = ['id']


    
@admin.register(Placement_Detail)
class PlacementAdmin(admin.ModelAdmin) : 
    list_display = ['id' ,'student' , 'company' , 'intern']
    readonly_fields = ['id']

        
@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin) : 
    list_display = ['id' ,'name']
    readonly_fields = ['id']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin) : 
    list_display = ['id' ,'name']
    readonly_fields = ['id']

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin) : 
    list_display = ['id' ,'name' ,'dream' ,'domain']
    readonly_fields = ['id']

