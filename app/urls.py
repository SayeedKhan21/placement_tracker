from django.urls import path ,include 
from .views import (
    HomeView ,
    ProfileView ,
    formListValues ,
)

app_name = 'app'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),    
    path('profile/<uuid:student_id>' , ProfileView.as_view(), name ='profile'),
    path('get_form_values' , formListValues ,name ='form-list' )
]


