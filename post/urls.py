from django.urls import path ,include 
from .views import (
    PostListView ,
    PostDetailView ,
)

app_name = 'post'
urlpatterns = [
    path('post/<uuid:pk>' , PostDetailView.as_view(), name ='post-detail'),
    # path('post/update/<int:pk>' , views.update_post, name ='update-post'),
    # path('post/delete/<int:pk>' , views.delete_post, name ='delete-post'),
    path('allposts/' ,PostListView.as_view(), name ='all-posts'),   
]
    