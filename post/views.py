from django.shortcuts import render
from django.views import generic
from .models import (
        Post ,
)
from app.models import (
    Company ,
    Domain ,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin ,
)
from django.urls import reverse 
from django.shortcuts import redirect
from django.views.generic import View
from django.urls import reverse
from .forms import (
    PostForm  ,
)
from app.models import (
    Placement_Detail ,
)
from django.contrib import messages
# Create your views here.

class PostListView(LoginRequiredMixin ,generic.ListView) : 

    model = Post
    context_object_name = 'posts'
    template_name = 'post/post_list.html'

    def get_context_data(self  , *args , **kwargs):
        context =  super().get_context_data(**kwargs)
        posts = Post.objects.all()

        cname = self.request.GET.get('company')
        dname = self.request.GET.get('domain')

        # print(cname ,dname)
        for p in posts : 
            print(p.offer.company)


        if cname and cname != 'All': 
            posts = posts.filter(offer__company__name = cname)

        if dname and dname != 'All': 
            posts = posts.filter(offer__company__domain__name = dname)

        # print(posts)

        context['posts'] = posts
        return context



class PostCreateView(LoginRequiredMixin ,View):
    
    def post(self ,request) : 
        form = PostForm(request.POST)         
       

    def get(self ,request) : 
        post_form = PostForm()
        context = { 
            'post_form' : post_form
        }
        return render(request, 'post/postcreate.html') 


class PostDeleteView(LoginRequiredMixin ,View) : 


    def get(self ,request) :
        return render(request ,'post/post_confirm_delete.html')


class PostUpdateView(LoginRequiredMixin , View) : 

    def post(self, request) : 
        form = PostForm(request.POST) 
        if form.is_valid() : 
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            ctc= form.cleaned_data['ctc']
            intern = form.cleaned_data['intern']
            company = form.cleaned_data['company']

          
        messages.success(request ,"Post Updated successfully")
        return redirect(reverse('app:profile'))
   
    def get(self, request) :
        data = ''
        form = PostForm(initial =data)
        return render(request , 'base/post_update.html' ,{'post_form' : form})

class PostDetailView( LoginRequiredMixin , generic.DetailView):

    model = Post 
    context_object_name = 'post'
