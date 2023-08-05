from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import UserLoginSerializer, UserSignUpSerializer, PostSerializer
from . models import User


# Create your views here.

def home(request):
    return HttpResponse("Your set up worked")

class Signup(APIView): #called a logic handling an signup 
    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'sign up successful'})
        return Response({'message' : 'an error occured', 'error' : serializer.errors})

class Login(APIView): #called a logic handling an login 
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            try : 
                user_to_login = User.objects.get(username=username)
            except Exception as e :
                return Response({'error' : str(e)})
            if user_to_login.password == password :
                return Response({'message' : 'login successful', 'user_data'  : UserLoginSerializer(user_to_login).data })
            return Response({'message' : 'wrong credentials'})
        return Response({'message' : 'the data sent to the api is not valid'})

class Post(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid() : 
            serializer.save()
            return Response({'message' : 'post has been created successfully', 'post_data'  :  serializer.data})
        return Response({'message'  : 'data sent to api is not valid'})