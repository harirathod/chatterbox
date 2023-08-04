from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """Returns the 'home.html' page when the request is made to this function."""
    # response = HttpResponse("Welcome to this blogging application!")
    return render(request, "home.html")
