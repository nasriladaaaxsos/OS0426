from django.urls import path     
from . import views

urlpatterns = [ 
    path('', views.index),
    path('create', views.create_appointment),
    path('edit', views.edit_appointment),
    path('viewall', views.view_all_appointment, name='showall'),
    path('delete', views.delete_appointment),
    path('viewupcomming', views.view_upcoming_appointment),#Ramez----viewing upcomming appointments
    path('details/<int:id>', views.appointment_detail),
    ]