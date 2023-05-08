

from django.urls import path, include
from .views import (
    CompanyListView ,
    CompanyDetailView ,
    StudentView ,
    PostView ,
    ProfileViewSet ,
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('profiles' , ProfileViewSet)

app_name = 'api'

urlpatterns = [
    path('',include(router.urls)),
    path('companies/' , CompanyListView.as_view() , name = 'get-companies') ,
    path('companies/<uuid:pk>/' , CompanyDetailView.as_view() , name = 'get-company') ,
    path('students/' , StudentView.as_view() ) ,
    path('posts/' , PostView.as_view() , name = 'posts') ,
]