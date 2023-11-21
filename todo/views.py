from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Todo
from .serializers import TodoSerializer


# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
  queryset = Todo.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = TodoSerializer
