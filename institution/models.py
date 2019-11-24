from django.db import models

# Create your models here.

class ChoiceList(models.Model):
    choices = models.CharField(max_length=200, default="Model Engineering College")


class Institution(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.ForeignKey(ChoiceList, on_delete=models.CASCADE)
    course = models.CharField(max_length=200, blank=False)
    duration = models.CharField(max_length=200, blank=False, default='4')

    def __str__(self):
          return self.name


