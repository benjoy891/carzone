from django.shortcuts import render
from django.http import HttpResponse  # This import may not be necessary for this particular view
from .models import Team

# Create your views here.

def home(request):
    teams = Team.objects.all()
    data = {
        'teams':teams,

    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams':teams,
    }
    return render(request, 'pages/about.html',data)

def cars(request):
    return render(request, 'pages/cars.html')

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')