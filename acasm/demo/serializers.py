from rest_framework import serializers
from . import models 

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.User
        fields = ('username', 'password')
        
class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.User
        fields = ('username', 'password')
        
