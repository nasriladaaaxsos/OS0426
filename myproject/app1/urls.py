from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.login, name='login'),
    path('create', views.create_appointment, name='create_appointment'),
    path('edit', views.edit_appointment, name='edit_appointment'),
    path('viewall', views.view_all_appointment, name='showall'),
    path('delete', views.delete_appointment, name='delete_appointment'),
    path('viewupcomming', views.view_upcoming_appointment, name='view_upcoming'),
    path('details/<int:id>', views.appointment_detail, name='appointment_detail'),
]




