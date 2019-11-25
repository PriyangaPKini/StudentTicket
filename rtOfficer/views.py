from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from rest_framework.response import Response
from rest_framework import status
from . models import RTOfficer
from students.models import Student
from .serializers import RTOfficerSerializer
from students.serializers import StudentSerializer



# class ApplicationList(APIView):
#     def get(self, request):
#         pending = Student.objects.filter(card=null)
#         serializer = StudentSerializer(,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer = RTOfficerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApplicationList(ListAPIView):
    serializer_class = StudentSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.filter(card = None)

