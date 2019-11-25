from django.shortcuts import render,redirect

from .models import Complaint
# from . models import Student
from .serializers import ComplaintSerializer
from rest_framework import generics

#
# # Create your views here.
# def complaint(request):
#     if request.method == 'POST':
#
#         busNumber = request.POST['busNumber']
#         message = request.POST['message']
#
#         complaint = Complaint( busNumber=busNumber, message=message)
#         complaint.save()
#
#         return redirect('')


class ComplaintList(generics.ListCreateAPIView):
    """Get/Add request
    get:
    Get all camps
    post:
    Add a camp
    """
    serializer_class = ComplaintSerializer
    queryset = Complaint.objects.all()