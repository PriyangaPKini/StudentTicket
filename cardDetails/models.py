from django.db import models

class CardDetails(models.Model):
    isApproved = models.BooleanField(default=False)
    dateOfIssue = models.DateField(null=True)
    dateOfExpiry = models.DateField(null=True)
    isCardValid = models.BooleanField(null=True, default=True)

    def __str__(self):
          return f'{self.id}'

