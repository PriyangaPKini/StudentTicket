from django.db import models
from datetime import datetime

# Create your models here.

class Complaint(models.Model):
    busNumber = models.CharField(max_length=20, blank=False)
    message = models.TextField(blank=True)
    complaint_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.complaint_date