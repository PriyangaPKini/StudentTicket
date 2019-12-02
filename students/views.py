from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models.signals import pre_save
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from rest_framework import generics
from students.models import Student
from cardDetails.models import CardInfo
import datetime
import json

# def create(request):
#
#     if request =='POST':
#         myfile = request.FILES.get('filename')
#         code = request.POST['id']
#         firstName = request.POST['name']
#         email = request.POST['email']
#         dob = request.POST['dob']
#         route = request.POST['route']
#         address = request.POST['address']
#
#     student = Student(code=code, firstName=firstName, email=email, dob=dob, route=route, address=address, image=myfile)
#     student.save()

def create_card(sender, instance, *args, **kwargs):
    card = CardInfo(sid=instance.code, dateOfIssue=datetime.date.today(), dateOfExpiry=datetime.date.today() + datetime.timedelta(6*365/12))
    card.save()
    instance.card = card

class StudentList(generics.ListCreateAPIView):

    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        # myfile = request.FILES.get('filename')
        code = data['code']
        firstName = data['firstName']
        # lastName = request.POST.get('lastName')
        email = data['email']
        # dob = request.POST.get('dob')
        route = data['route']
        address = data['address']
        # student = Student(code=code, firstName=firstName, lastName=lastName,email=email, dob=dob, route=route, address=address, image=myfile)
        student = Student(code=code, firstName=firstName, email=email, route=route, address=address)
        student.save()

        return redirect('/students')


pre_save.connect(create_card, sender=Student)


class IndividualView(generics.RetrieveAPIView):
    """Get info about a student
    """
    serializer_class = StudentSerializer
    lookup_url_kwarg = 'id'

    def perform_create(self, serializer):
        id = self.kwargs.get(self.lookup_url_kwarg)
        serializer.save(student=Student.objects.get(id=id))

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        student = Student.objects.get(code=id)
        # serializer = self.get_serializer(student)
        # print(serializer.data)
        return student
