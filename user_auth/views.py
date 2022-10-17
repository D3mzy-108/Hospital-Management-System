from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def login(request):
    return HttpResponse("<h1>Login Page</h1><br><a href='/dashboard/D3mzy-108/'>Patient Dashboard</a><br><a href='/dashboard/Demzy-108/'>Doctor Dashboard</a>")


def signup(request):
    return HttpResponse("<h1>Register Page</h1>")
