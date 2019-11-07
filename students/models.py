from django.db import models
from datetime import datetime

# Create your models here.
class Student(models.Model):
     stud_id = models.IntegerField(primary_key=True)
     firstName = models.CharField(max_length=200)
     lastName = models.CharField(max_length=200)
     email= models.CharField(max_length=50)
     dob = models.DateField()
     # age = models.IntegerField(null=False)
     nameOfInstitution = models.CharField(max_length=200)
     courseOfStudy = models.CharField(max_length=200)
     durationOfCourse = models.CharField(max_length=200)
     dateOfIssue = models.DateField()
     dateOfExpiry = models.DateField()
     isCardValid = models.BooleanField()
     isApproved = models. BooleanField()
     startingpoint1 = models.CharField(max_length=250,blank=True)
     endingpoint1 = models.CharField(max_length=250,blank=True)
     startingpoint2 = models.CharField(max_length=250,blank=True)
     endingpoint2 = models.CharField(max_length=250,blank=True)
     startingpoint3 = models.CharField(max_length=250,blank=True)
     endingpoint3 = models.CharField(max_length=250,blank=True)
     startingpoint4 = models.CharField(max_length=250,blank=True)
     endingpoint4 = models.CharField(max_length=250,blank=True)

     def __str__(self):
          return self.firstName +" " + self.lastName
