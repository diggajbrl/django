from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def app (request) :

    data = {
        'title' : 'H O M E'
    }

    return render (request, 'index.html', data)

def service (request) :
    
    data = {
        'title' : 'S E R V I C E'
    }

    return render (request, 'service.html', data)

def info (request) :
    
    data = {
        'title' : 'I N F O'
    }

    return render (request, 'info.html', data)

def about (request) :
    
    data = {
        'title' : 'A B O U T'
    }

    return render (request, 'about.html', data)

def contact (request) :
    
    data = {
        'title' : 'C O N T A C T'
    }

    return render (request, 'contact.html', data)