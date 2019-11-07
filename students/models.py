from django.db import models
from datetime import datetime

# Create your models here.
class Student(models.Model):
     stud_id = models.IntegerField(max_length=6,primary_key=True)
     firstName = models.CharField(max_length=200)
     lastName = models.CharField(max_length=200)
     email= models.CharField(max_length=50)
     nameOfInstitution = models.CharField(max_length=200)
     dateOfIssue = models.DateTimeField(default= datetime.now,blank=True)
     dateOfExpiry = models.DateTimeField()
     courseOfStudy = models.CharField(max_length=200)
     isValid = models.BooleanField()
     isApproved = models. BooleanField()
     startingpoint1 = models.CharField(max_length=250)
     endingpoint1 = models.CharField(max_length=250)
     # age = models.IntegerField(null=False)
     dob = models.DateField()
     durationOfCourse = models.CharField(max_length=200)
     startingpoint2 = models.CharField(max_length=250)
     endingpoint2 = models.CharField(max_length=250)
     startingpoint3 = models.CharField(max_length=250)
     endingpoint3 = models.CharField(max_length=250)
     startingpoint4 = models.CharField(max_length=250)
     endingpoint4 = models.CharField(max_length=250)

     def __self(self):
         return self.stud_id
