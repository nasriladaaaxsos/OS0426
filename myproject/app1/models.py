from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    dateOfBirth = models.DateField()
    created_At = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
#Class User
# Class attributes: username, password, dateOfBirth, created_At, updated_At



#Class Appointment 
# Class attributes: Appointment_Desc, Appointment_Date, created_At, updated_At
class Appointment(models.Model) :
    Appointment_Desc = models.TextField()
    Appointment_Date = models.DateField()
    created_at = models.DateTimeField(auto_now=True)
    updated_At = models.DateTimeField(auto_now_add=True)



def edit_data(data,id):
    appointment = Appointment.objects.get(id = id )
    appointment.desc =data['desc']
    appointment.date = data['date']
    appointment.save()