from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Institution(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'
    

class DegreeType(models.Model):
    degree = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.degree}'
    

class Major(models.Model):
    majorName = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.majorName}'
    

class Country(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'
    

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    degreeType = models.ForeignKey(DegreeType, on_delete=models.CASCADE)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    lookingFor = models.CharField(max_length=50, choices=(
        ('internship', 'internship'),
        ('collaborate on a project','collaborate on a project')
    ))
    date_avaiable =models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.user.lastname},{self.user.firstname}'
    

