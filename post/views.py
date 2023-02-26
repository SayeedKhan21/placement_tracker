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
# Create your views here.

class PostListView(generic.ListView) : 

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


# @login_required(login_url='login')
# def create_post(request):
#      if request.method == 'POST' : 
#         form = PostForm(request.POST)         
#         if form.is_valid() : 
#             usr = request.user
#             stu =''
#             for s in  Student.objects.raw("SELECT * FROM student WHERE user_id = %s" ,[usr.id]) :
#                 stu =  s.id
#             name = form.cleaned_data['company']
#             print(name)
#             intern = form.cleaned_data['intern']
#             ctc = form.cleaned_data['ctc']
#             for c in Company.objects.raw("SELECT * FROM Company WHERE name = %s" ,[name]):
#                 company = c.id
#             with connection.cursor() as cursor  : 
#                 cursor.execute("INSERT INTO Placement_Detail(ctc_stipend ,intern,company_id_id,student_id_id) VALUES (%s,%s,%s,%s)"  ,
#                 [ctc,intern,company,stu])
#             for res in Placement_Detail.objects.raw("SELECT * FROM Placement_Detail order by id desc LIMIT 1") : 
#                 offer = (res)       
#             form.save(offer_id = offer)
#             new_offer = (stu  ,company  ,ctc , intern ,offer)
#             print("------ NEW OFFER CREATED ------")
#             print(new_offer)
#             return redirect(reverse('profile' ,kwargs={"pk" : stu}))

#      else :
#         post_form = PostForm()
#         context = { 
#             'post_form' : post_form
#         }
#      return render(request, 'base/postcreate.html') 


# @login_required(login_url='login')
# def delete_post(req ,pk) : 
#     with connection.cursor() as cursor : 
#         cursor.execute("SELECT id FROM student WHERE user_id = %s " ,[req.user.id])
#         stuid = cursor.fetchone()[0]
#     if req.method == 'POST' : 
#         with connection.cursor() as cursor : 
#             cursor.execute("SELECT offer_id_id from posts WHERE id =%s" ,[pk])
#             pid = cursor.fetchone()[0]
#             cursor.execute("DELETE FROM posts WHERE id =%s" ,[pk])
#             cursor.execute("DELETE FROM Placement_Detail WHERE id =%s" ,[pid])
#             return redirect(reverse('profile' , kwargs={'pk' : stuid}))
#     elif req.method == 'GET' : 
#         return render(req ,'base/post_confirm_delete.html' ,{'id' :stuid})

# @login_required(login_url='login')
# def update_post(req , pk) : 
#     with connection.cursor() as cursor : 
#         cursor.execute("SELECT id FROM student WHERE user_id = %s " ,[req.user.id])
#         stuid = cursor.fetchone()[0]
#     if req.method == 'POST' : 
#         form = PostForm(req.POST) 
#         if form.is_valid() : 
#             title = form.cleaned_data['title']
#             content = form.cleaned_data['content']
#             ctc= form.cleaned_data['ctc']
#             intern = form.cleaned_data['intern']
#             company = form.cleaned_data['company']

#             print("updated intern = " , intern)

#             for p in  Placement_Detail.objects.raw("SELECT * FROM Placement_Detail WHERE id =  (SELECT offer_id_id from posts WHERE id = %s)" ,[pk]) : 
#              pobj = p  
#             print("POBJ id = " , pobj.id)
#             print("initial intern =" ,pobj.intern)
#             for d in Company.objects.raw("SELECT id FROM Company WHERE name = %s" ,[company]) : 
#                 company_obj = d
            
#             same = True
#             if pobj.company_id.name != company or pobj.ctc_stipend != ctc or pobj.intern != intern :
#                 same = False 
#             print("same = " ,same)
#             if same == False : 
#                 with connection.cursor() as cursor : 
#                     cursor.execute("UPDATE Placement_Detail SET company_id_id =%s , ctc_stipend =%s ,intern =%s WHERE id =%s" ,[company_obj.id ,ctc ,intern,pobj.id])
                    
            
#             updated_time = datetime.now()
#             with connection.cursor() as cursor : 
#                 cursor.execute("UPDATE posts SET title=%s ,content=%s  ,updated_at=%s WHERE offer_id_id =%s" ,[title,content,updated_time ,pobj.id])
#         messages.success(req ,"Post Updated successfully")
#         return redirect(reverse('profile' ,kwargs={'pk' : stuid }))
#     elif req.method == 'GET' :
#         for p in Post.objects.raw("SELECT * FROM posts WHERE id = %s" ,[pk]):
#             post_object = p 
#         for p in Placement_Detail.objects.raw("SELECT * FROM Placement_Detail WHERE id =(SELECT offer_id_id FROM posts WHERE id =%s)" ,[pk]) : 
#             placement_object = p
#         data = {
#         "title" : f"{post_object.title}",
#         "content" : f"{post_object.content}",
#         "ctc":f"{placement_object.ctc_stipend}",
#         "intern":f"{placement_object.intern}",
#         "company":f"{placement_object.company_id}",
#          }
#         print(data)
#         form = PostForm(initial =data)
#         return render(req , 'base/post_update.html' ,{'post_form' : form})

class PostDetailView( LoginRequiredMixin , generic.DetailView):

    model = Post 
    context_object_name = 'post'
