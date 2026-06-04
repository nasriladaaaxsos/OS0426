from django.shortcuts import render, redirect, HttpResponse
from . import models

#Get
#Landing page for login
def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = models.User.objects.filter(username=username, password=password).first()
        if user:
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect('showall')

        return render(request, 'index.html', {
            'error': 'Wrong username or password'
        })

    
    return render(request, 'index.html')



#Get
def view_all_appointment(request):
    return render(request, 'viewappointments.html')

#Get
def create_appointment(request):
    if request.method == 'POST' :
        Appointment_Desc = request.POST['Appointment_Desc']
        Appointment_Date = request.POST['Appointment_Date']
        models.Appointment.objects.create(
            Appointment_Desc=Appointment_Desc,
            Appointment_Date=Appointment_Date
        )
        return redirect('/')
    else :
        return render(request, 'createappointment.html')

#Get
def edit_appointment(request):
    if request.method == "POST":
        models.edit_data(request.POST, request.POST['appointment_id'])
        return redirect('/edit')
    return render(request, 'editappointment.html')

#Post request
def delete_appointment(request):
    return redirect('showall')

def view_upcoming_appointment(request):
    return render(request, 'viewupappointments.html')


def appointment_detail(request, id):
    appointment = models.Appointment.objects.get(id = id)
    context = {
        "appointment" : appointment
    }
    return render(request, 'detail.html',context)

