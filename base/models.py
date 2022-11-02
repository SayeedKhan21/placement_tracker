from django.db import models
from django.contrib.auth.models import User

class Department(models.Model) : 
    name = models.CharField(max_length=100)
    def __str__(self) :
        return self.name

import datetime

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year
years = year_choices()

class Student(models.Model) :
    name = models.CharField(max_length=100)
    year_of_passing =models.IntegerField(('year_of_passing'), choices=years, default=current_year)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)

class Domain(models.Model) : 
    name = models.CharField(max_length=100)

class Company(models.Model) :
    name = models.CharField(max_length=100)
    dream = models.BooleanField(default=False)
    domain_id = models.ForeignKey(Domain, on_delete=models.CASCADE)
    class Meta :
        verbose_name = ("Company")
        verbose_name_plural = ("Companies")
    
class Placement_Detail(models.Model) :
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    ctc_stipend = models.IntegerField()
    intern = models.BooleanField()

class Post(models.Model) :
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta : 
        db_table = 'posts'

    def __str__(self) :
        return self.title