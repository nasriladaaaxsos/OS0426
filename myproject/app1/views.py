from django.shortcuts import render, redirect
from .models import User

def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password).first()
        if user:
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect('showall')

        return render(request, 'index.html', {
            'error': 'Wrong username or password'
        })

    return redirect('home')


def view_all_appointment(request):
    return render(request, 'viewappointments.html')


def create_appointment(request):
    return render(request, 'createappointment.html')


def edit_appointment(request):
    if request.method == "POST":
        edit_data(request.POST, request.POST['appointment_id'])
        return redirect('/edit')
    return render(request, 'editappointment.html')


def delete_appointment(request):
    return redirect('showall')


def view_upcoming_appointment(request):
    return render(request, 'viewupappointments.html')


def appointment_detail(request, id):
    return render(request, 'detail.html')