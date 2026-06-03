from django.db import models
from datetime import date

# Create your models here.

#Class User
# Class attributes: username, password, dateOfBirth, created_At, updated_At
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    dateOfBirth = models.DateField()
    created_At = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)
#Class Appointment 
# Class attributes: Appointment_Desc, Appointment_Date, created_At, updated_At
class Appointment(models.Model):
    Appointment_Desc = models.TextField(default="")
    Appointment_Date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)