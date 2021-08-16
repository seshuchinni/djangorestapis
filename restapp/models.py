from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Student(models.Model):
    name  = models.CharField(max_length=50)
    age = models.IntegerField()
    fathername = models.CharField(max_length=50)

