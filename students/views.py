from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Student
from .serializers import StudentSerializer
from rest_framework import generics

class StudentList(generics.ListCreateAPIView):
    """Get/Add request
    get:
    Get all camps
    post:
    Add a camp
    """

    serializer_class = StudentSerializer
    queryset = Student.objects.all()
