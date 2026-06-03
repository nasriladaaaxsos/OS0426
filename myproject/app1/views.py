from django.shortcuts import render, redirect, HttpResponse
from .models import *
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
    if request.method == "POST":
        edit_data(request.POST, request.POST['appointment_id'])
        return redirect('/edit')
    return render(request, 'editappointment.html')

#Post request
def delete_appointment(request):
    return redirect('showall')

def view_upcoming_appointment(request):
    return render(request, 'viewupappointments.html')

def appointment_detail(request, id):
    return render(request, 'detail.html')

