from . models import Todo
from rest_framework import serializers
from django.contrib.auth.models import User

class TodoSerializer(serializers.HyperlinkedModelSerializer):
   user = serializers.CurrentUserDefault()
   class Meta:
       model = Todo
       fields = ['id', 'title', 'description', 'created_at', 'user']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']