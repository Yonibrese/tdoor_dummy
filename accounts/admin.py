from django.contrib import admin
from . import models
# Register your models here.

class InstitutionAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(models.Institution, InstitutionAdmin)


class DegreeTypeAdmin(admin.ModelAdmin):
    list_display = ['degree']

admin.site.register(models.DegreeType, DegreeTypeAdmin)

class MajorAdmin(admin.ModelAdmin):
    list_display = ['majorName']

admin.site.register(models.Major, MajorAdmin)

class CountryAdmin(admin.ModelAdmin):
    lsit_display = ['name']

admin.site.register(models.Country, CountryAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(models.Student, StudentAdmin)