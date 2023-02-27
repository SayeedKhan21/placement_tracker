from django.shortcuts import render
from django.views.generic import (
    View ,
    DetailView ,
)
from django.http import JsonResponse
from post.models import (
    Post ,
)
from .models import (
    Student ,
    Company ,
    Domain ,
)
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomeView(View):

    def get(self,request) : 
    
        posts = Post.objects.all()
        posts = posts[:min(4 , len(posts))]    
        print(posts)
        context ={
            'posts' : posts
        }
        return render(request, 'app/home.html', context) 
    


class ProfileView(LoginRequiredMixin ,View) : 
    
    def get(self,req , student_id):
        student = Student.objects.get(id = student_id)
        context = {}
        posts = Post.objects.filter(offer__student__user = self.request.user)
        context['posts'] = posts
        context['student'] = student
        return render(req , 'app/profile.html' ,context)
    


def formListValues(request) : 
    res = {}
    companyList = []
    domainList = []
    for c in  Company.objects.values() : 
        companyList.append((c['name']))
    res['companies'] = companyList
    for d in Domain.objects.values() : 
        domainList.append(d['name'])
    res['domains'] = domainList
    return JsonResponse(res , safe=False)