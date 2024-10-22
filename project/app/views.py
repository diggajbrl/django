from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def app (request) :
    return render (request, 'index.html')

def service (request) :
    return render (request, 'service.html')

def info (request) :
    return render (request, 'info.html')

def about (request) :
    return render (request, 'about.html')

def contact (request) :
    return render (request, 'contact.html')