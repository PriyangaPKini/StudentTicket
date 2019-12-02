from django.db import models

class CardInfo(models.Model):
    sid = models.IntegerField(null=True)
    isApproved = models.BooleanField(default=False)
    dateOfIssue = models.DateField(null=True)
    dateOfExpiry = models.DateField(null=True)
    isCardValid = models.BooleanField(default=True)

    def __str__(self):
          return f'{self.id}'

