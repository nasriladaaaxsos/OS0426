from django.shortcuts import render, redirect, HttpResponse
from . import models

#Get
#Landing page for login
def index(request):
    return render(request, 'index.html')

#Get
def view_all_appointment(request):
    return render(request, 'viewappointments.html')

#Get
def create_appointment(request):
    return render(request, 'createappointment.html')

#Get
def edit_appointment(request):
    return render(request, 'editappointment.html')

#Post request
def delete_appointment(request):
    return redirect('showall')

#Ramez----viewing upcomming appointments
def view_upcoming_appointment(request):
    # Get the upcoming appointments using the model function
    context = {
        'appointments': models.upcomming_appointment()
    }
    return render(request, 'viewupappointments.html', context)

def appointment_detail(request, id):
    return render(request, 'detail.html')

