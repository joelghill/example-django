from django.shortcuts import render, HttpResponse

def home(request, **kwargs):
    return HttpResponse("Hello")
