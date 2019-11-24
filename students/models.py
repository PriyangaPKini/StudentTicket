from django.db import models
from datetime import datetime

# Create your models here.
def uploadImage(instance,filename):
     return "students/photos/{firstName}_{id}/{filename}".format(firstName=instance.firstName,id=instance.id,filename=filename)


class Student(models.Model):
     id = models.AutoField(primary_key=True)
     code = models.CharField(max_length=10, blank=False)
     firstName = models.CharField(max_length=200, blank=False)
     lastName = models.CharField(max_length=200, blank=False)
     email= models.CharField(max_length=50, unique=True, blank=False)
     dob = models.DateField(blank=False)
     image = models.ImageField(upload_to=uploadImage, blank=False,null=True)
     start1 = models.CharField(max_length=250, blank=True)
     stop1 = models.CharField(max_length=250, blank=True)
     start2 = models.CharField(max_length=250, blank=True)
     stop2 = models.CharField(max_length=250, blank=True)
     start3 = models.CharField(max_length=250, blank=True)
     stop3 = models.CharField(max_length=250, blank=True)
     start4 = models.CharField(max_length=250, blank=True)
     stop4 = models.CharField(max_length=250, blank=True)

     def __str__(self):
          return  self.firstName +" " + self.lastName

