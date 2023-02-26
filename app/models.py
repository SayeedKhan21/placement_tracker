from django.db import models
from base.models import (
    BaseModel ,
)

from .helpers import (
    years ,
    current_year ,
)
from django.conf import settings


# Create your models here.
class Domain(BaseModel) : 
    name = models.CharField(max_length=100)

    def __str__(self) :
        return self.name
  

class Department(BaseModel) : 
    name = models.CharField(max_length=100)
    
    def __str__(self) :
        return self.name


class Company(BaseModel) :
    name = models.CharField(max_length=100)
    dream = models.BooleanField(default=False)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)

    
    def __str__(self) :
        return self.name

    class Meta : 
        verbose_name_plural = 'companies'
  
    
class Student(BaseModel) :
    name = models.CharField(max_length=100)
    year_of_passing =models.IntegerField(('year_of_passing'), choices=years, default=current_year)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL ,on_delete = models.CASCADE ,related_name ='student')

    
    def __str__(self) :
        return self.name


class Placement_Detail(BaseModel) :
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    amount = models.IntegerField()
    intern = models.BooleanField()

    
    def __str__(self) :
        return str(self.student) + 'Placed in ' + str(self.company) 
  