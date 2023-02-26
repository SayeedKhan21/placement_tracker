from django.shortcuts import render ,redirect 
from django.urls import reverse
from .models import *
from django.contrib.auth.models import User
from .forms import *
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login ,logout,authenticate


class LoginView(View):

    def post(self,request):
        form = LoginForm(request.POST) 
        if form.is_valid() : 

            data = {
                'name' : form.cleaned_data['name'] ,
                'password' : form.cleaned_data['password']
            }

            try : 
                stu  = Student.objects.filter(**data)
            except Student.DoesNotExist : 
                messages.warning(request , 'User Does Not Exist')
                return redirect('login')
            
            stu = authenticate(request , username = data['name'] ,password = data['password'])
            if stu is not None : 
                login(request , stu)
                messages.success(request, 'Logged In Sucessfully')
                return redirect('home')       
        
        messages.warning(request , 'Invalid credentials')
        context = {
              'form' : form
        }
        return render(request , 'base/login.html' ,context)

    def get(self ,request):
        print("here")
        form = LoginForm()
        return render(request , 'base/login.html' , {'form' : form})

   
class LogoutView(LoginRequiredMixin , View) : 
    def get(self,req) : 
        logout(req)
        return redirect(reverse('app:home'))



class  RegisterView(View) : 

    def get(self,request) : 
        form = RegisterForm()
        context = { 
            'form' : form
        }
        return render(request, 'base/register.html') 

    def post(self,request) : 
        form = RegisterForm(request.POST)
        if form.is_valid() : 

            payload = {
                'name' : form.cleaned_data['name'],
                'password' : form.cleaned_data['password'],
                'yop' : form.cleaned_data['year_of_passing'],
                'dept_id' : form.cleaned_data['dept']
            }

            user =User.objects.create(username = payload['name'])
            user.set_password(payload['password'])
            user.save()
           
            stu = Student.objects.create(
               **payload
            )
            print(f"Student created with name{payload['name']} ")
            return redirect('login')
        else :
            context = { 
                'form' : form
            }
            return render(request, 'base/register.html', context) 


# 