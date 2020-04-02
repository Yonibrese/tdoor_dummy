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


class Industry(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    degreeType = models.ForeignKey(DegreeType, on_delete=models.CASCADE)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    lookingFor = models.CharField(max_length=100, choices=(
        ('internship', 'internship'),
        ('collaborate on a project', 'collaborate on a project')
    ))
    date_avaiable = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.user.lastname},{self.user.firstname}'


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    companyName = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company/logo/%Y/%m/%d', null=True, blank=True)
    num_of_employees = models.IntegerField(null=True, blank=True)
    lookingTo = models.CharField(max_length=100, choices=(
        ('hire interns', 'hire interns'),
        ('hire employees','hire employees'),
        ('both', 'both')
    ))
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    videoURL = models.URLField(null=True, blank=True)
    webURL = models.URLField(null=True, blank=True)
