from django.urls import path ,include 
from .views import (
    PostListView ,
    PostDetailView ,
    PostUpdateView ,
    PostDeleteView ,
)

app_name = 'post'
urlpatterns = [
    path('post/<uuid:pk>' , PostDetailView.as_view(), name ='post-detail'),
    path('post/update/<uuid:pk>' , PostUpdateView.as_view(), name ='update-post'),
    path('post/delete/<uuid:pk>' , PostDeleteView.as_view(), name ='delete-post'),
    path('allposts/' ,PostListView.as_view(), name ='all-posts'),   
]
    