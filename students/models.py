from django.db import models
from datetime import datetime
from cardDetails.models import CardInfo
from institution.models import Institution

# Create your models here.
def uploadImage(instance,filename):
     return "students/photos/{firstName}_{id}/{filename}".format(firstName=instance.firstName, id=instance.id, filename=filename)


class Student(models.Model):
     id = models.AutoField(primary_key=True)
     code = models.CharField(max_length=10, blank=False, null=True)
     firstName = models.CharField(max_length=200, blank=False, null=True)
     lastName = models.CharField(max_length=200, blank=False, null=True)
     email= models.CharField(max_length=50, unique=True, blank=False, null=True)
     dob = models.DateField(blank=False, null=True)
     image = models.ImageField(upload_to=uploadImage, blank=False, null=True)
     route = models.CharField(max_length=500, blank=True, null=True)
     # start1 = models.CharField(max_length=250, blank=True, null=True)
     # stop1 = models.CharField(max_length=250, blank=True, null=True)
     # start2 = models.CharField(max_length=250, blank=True, null=True)
     # stop2 = models.CharField(max_length=250, blank=True, null=True)
     # start3 = models.CharField(max_length=250, blank=True, null=True)
     # stop3 = models.CharField(max_length=250, blank=True, null=True)
     # start4 = models.CharField(max_length=250, blank=True, null=True)
     # stop4 = models.CharField(max_length=250, blank=True, null=True)
     card = models.OneToOneField(CardInfo, on_delete=models.CASCADE, blank=True, null=True)
     institution = models.ForeignKey(Institution, on_delete=models.CASCADE, blank=True, null=True)

     def __str__(self):
          return  self.firstName +" " + self.lastName

