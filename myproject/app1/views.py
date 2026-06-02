from django.shortcuts import render, redirect, HttpResponse
from . import models

# Create your views here.
def index(request):
    return render(request, 'index.html')