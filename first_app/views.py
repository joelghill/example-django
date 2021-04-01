from django.shortcuts import render
from django.template.response import SimpleTemplateResponse
from datetime import datetime


def get_current_time(request):
    current_time = datetime.now()
    timezone = request.GET.get('timezone')

    the_data = {
        'current_time': current_time,
        'timezone': timezone
    }

    response = SimpleTemplateResponse('current_time.html', the_data)
    return response

def hello_world(request, name, number):
    current_time = datetime.now()

    the_data = {
        'current_time': current_time,
        'name': name,
        'number': number
    }
    return SimpleTemplateResponse('current_time.html', the_data)
