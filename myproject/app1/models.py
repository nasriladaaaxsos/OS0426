from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    dateOfBirth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Appointment(models.Model):
    Appointment_desc = models.CharField(max_length=200)
    Appointment_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def edit_data(data,id):
    appointment = Appointment.objects.get(id = id )
    appointment.desc =data['desc']
    appointment.date = data['date']
    appointment.save()
    
