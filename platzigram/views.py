"""Platzigram views"""
#Django
from django.urls import path
from django.http import HttpResponse, JsonResponse

#"Utilities"
from datetime import datetime
import json


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! current server time is {now}'.format(now=now))


def sort_int(request):
    print(request)
    numbers = request.GET['numbers']
    numbers = [int(x) for x in numbers.split(',')]
    #pdb.set_trace()  # realtime debugger
    #return HttpResponse('Hii the numbers are: {}, the sorted list are {}'.format(numbers, sorted(numbers)))
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers' : sorted_ints,
        'message': 'Integers sorted succesfully'
    }
    return HttpResponse(json.dumps(data), content_type='application/json')
    #return JsonResponse({'numbers': sorted(numbers)})



def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Welcome {}.'.format(name)

    return HttpResponse(message)

