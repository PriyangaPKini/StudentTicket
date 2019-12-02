from django.db import models
from datetime import datetime

# Create your models here.

class Complaint(models.Model):
    busNumber = models.CharField(max_length=20, blank=False, null=True)
    message = models.TextField(blank=True, null=True)
    complaint_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.complaint_date