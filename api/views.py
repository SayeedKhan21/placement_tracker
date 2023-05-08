from django.shortcuts import render
from .serializers import (
    CompanyListSerializer ,
    CompanyDetailSerializer ,
    StudentSerializer,
    StudentProfileSerializer ,
    PostListSerializer ,
)
from app.models import ( 
    Company ,
    Student ,
    StudentProfile ,
)
from post.models import ( 
    Post ,
)
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
# Create your views here.

class CompanyListView(generics.ListAPIView) : 

    serializer_class  = CompanyListSerializer
    queryset = Company.objects.all()

class CompanyDetailView(generics.RetrieveAPIView) : 

    serializer_class = CompanyDetailSerializer
    queryset = Company.objects.all()
    
class StudentView(APIView) :


    def get(self ,request) : 
        students = Student.objects.all()
        serializer = StudentSerializer(students , many = True)
        return Response(serializer.data ,status=status.HTTP_200_OK)
    
    def post(self ,request) :
        student_data = request.data 
        serializer = StudentSerializer(data=student_data ,context={'user' : student_data['user']})
        if serializer.is_valid () :
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     

    
class ProfileViewSet(viewsets.ModelViewSet) : 

    serializer_class = StudentProfileSerializer
    queryset = StudentProfile.objects.all()



class PostView(APIView) : 

    def get(self ,request) : 
        posts = Post.objects.all()
        serializer = PostListSerializer(posts , many =True)
        return Response(serializer.data , status = status.HTTP_200_OK)


    def post(self, request) : 

        offer_data = request.data.pop("offer")

        serializer = PostListSerializer(data =request.data ,context={'offer' : offer_data})
        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView) : 


    def post(self, request) : 
        pass

class LogoutView(APIView) : 

    def post(self, request) : 
        pass


