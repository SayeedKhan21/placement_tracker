from django.shortcuts import render ,redirect 
from django.urls import reverse
from .models import *
from django.contrib.auth.models import User
from .forms import *
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login ,logout,authenticate
from django.contrib.auth import get_user_model

class LoginView(View):

    def post(self,request):
        form = LoginForm(request.POST) 
        if form.is_valid() : 

            data = {
                'username' : form.cleaned_data['name'] ,
                'password' : form.cleaned_data['password']
            }

            try : 
                user  = get_user_model().objects.filter(**data)
            except User.DoesNotExist : 
                messages.warning(request , 'User Does Not Exist')
                return redirect('login')
            
            user = authenticate(request , username = data['username'] ,password = data['password'])
            if user is not None : 
                login(request , user)
                messages.success(request, 'Logged In Sucessfully')
                return redirect('app:home')       
        
        messages.warning(request , 'Invalid credentials')
        context = {
              'form' : form
        }
        return render(request , 'base/login.html' ,context)

    def get(self ,request):
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
        return render(request, 'base/register.html' ,context) 

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