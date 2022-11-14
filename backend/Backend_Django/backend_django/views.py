#Django
from django.http import HttpResponse, JsonResponse

#Utilities
from datetime import datetime

def hello_world(request):

    return HttpResponse('Hello, world! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M')
    ))


def hi(request):

    numbers = request.GET['numbers']
    return HttpResponse(numbers, status = 200)

def testActuator(request):

    print('llego aqui')
    print(request.body.decode('utf-8'))

    return JsonResponse({'command': 'OK'}, status = 200)