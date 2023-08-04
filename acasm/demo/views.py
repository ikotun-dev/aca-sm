from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import UserLoginSerializer, UserSignUpSerializer


# Create your views here.

def home(request):
    return HttpResponse("Your set up worked")

class Signup(APIView):
    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'sign up successful'})
        return Response({'message' : 'an error occured', 'error' : serializer.errors})

