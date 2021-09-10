from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import generic

# Create your views here.
def LoginView(request):
    return render(request, "noah/login.html")



