from django.db import models
from django.utils import timezone

# Create your models here.

#Class User
# Class attributes: username, password, dateOfBirth, created_At, updated_At

#Class Appointment 
# Class attributes: Appointment_Desc, Appointment_Date, created_At, updated_At
# class Appointment(models.Model):
#     Appointment_Desc = models.CharField(max_length=255)
#     Appointment_Date = models.DateTimeField()
#     created_At = models.DateTimeField(auto_now_add=True)
#     updated_At = models.DateTimeField(auto_now=True)


#Ramez----function to get upcomming appointments
def upcomming_appointment():
    today = timezone.now().date()
    return Appointment.objects.filter(Appointment_Date__date__gte=today).order_by('Appointment_Date')