from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def admins(request):
    return HttpResponse("Admin Panel")
