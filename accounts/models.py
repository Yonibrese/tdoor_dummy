from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Institution(models.Model):
    name = models.CharField(max_length=200)

class DegreeType(models.Model):
    degree = models.CharField(max_length=200)

class Major(models.Model):
    majorName = models.CharField(max_length=200)

class Country(models.Model):
    name = models.CharField(max_lenght=200)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    degreeType = models.ForeignKey(DegreeType, on_delete=models.CASCADE)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)

