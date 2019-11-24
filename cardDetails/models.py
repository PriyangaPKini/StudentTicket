from django.db import models
from students.models import Student
from institution.models import Institution
# Create your models here.
class CardDetails(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    # institution = models.OneToOneField(Institution, on_delete=models.CASCADE, related_name='institution')
    isApproved = models.BooleanField(default=False)
    dateOfIssue = models.DateField(null=True)
    dateOfExpiry = models.DateField(null=True)
    isCardValid = models.BooleanField(null=True, default=True)

    def __str__(self):
          return " "

