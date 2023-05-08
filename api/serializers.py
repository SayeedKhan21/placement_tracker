from rest_framework import serializers
from django.contrib.auth import get_user_model
from app.models import * 
from post.models import *
from rest_framework.exceptions import ValidationError


class DepartmentSerializer(serializers.ModelSerializer) : 

    class Meta : 
        model = Department
        fields = ('name',)

class StudentSerializer(serializers.ModelSerializer) : 

    dept = DepartmentSerializer()

    class Meta : 
        model = Student
        fields = ('id' ,'name', 'year_of_passing' ,'dept')
        extra_fields = ['user']

    def validate(self, attrs):
        user_email = self.context['user']['email']
        exists = get_user_model().objects.filter(email = user_email)
        if exists : 
            raise ValidationError("User with the email already exists")
        return super().validate(attrs)


    def create(self, validated_data):
        
        user_data = validated_data.pop("user")
        department = dict(validated_data.pop("dept"))
        dept = Department.objects.create(**department)
        user = get_user_model().objects.create(**user_data)
        student = Student.objects.create(**validated_data , user = user ,dept = dept)
        return student
    
    def update(self, instance, validated_data):
      
        return super().update(instance, validated_data)

class StudentProfileSerializer(serializers.ModelSerializer) : 

    student = serializers.SerializerMethodField()
    
    class Meta : 
        model = StudentProfile
        fields = ('id' , 'avatar' , 'bio' , 'student')

    def get_student(self , instance) : 

        student = StudentSerializer(instance.student).data
        del student['id']
        return student
    
    def update(self, instance,validated_data) : 
        instance.avatar = validated_data.get('avatar' , instance.avatar)
        instance.bio = validated_data.get('bio' , instance.bio)
        instance.save()
        return instance


class CompanyListSerializer(serializers.ModelSerializer) : 

    class Meta : 
        model = Company
        fields = ('id' ,'name' , 'logo')


class CompanyDetailSerializer(serializers.ModelSerializer) : 

    class Meta : 
        model = Company
        fields =('name' , 'dream' ,'domain' , 'description' , 'link' ,'logo')



class OfferSerializer(serializers.ModelSerializer) : 

    # student = StudentSerializer()
    # company = CompanyDetailSerializer()

    class Meta : 
        model = Placement_Detail
        fields = ('student' , 'company')

class PostListSerializer(serializers.ModelSerializer) :

    student = serializers.SerializerMethodField()

    class Meta : 
        model = Post
        fields = ('title' ,'content' ,'student')

    
    def get_student(self ,instance) : 
        student_instance = instance.offer.student
        student = StudentSerializer(student_instance).data
        del student['dept']
        del student['year_of_passing']
        student['created_at'] = student_instance.created_at
        return student


class PostDetailSerializer(serializers.ModelSerializer) :

    offer = OfferSerializer()


    class Meta : 
        model = Post 
        fields = ('title' ,'offer' ,'content')




    def create(self, validated_data):
        print(self.context['offer'])
        return super().create(validated_data)
    