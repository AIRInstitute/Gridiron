import logging
import requests
from rest_framework import status
from rest_framework.response import Response

#Django
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from core import clients as client

logger = logging.getLogger(__name__)

def get_entities(request):
    
    orionClient = client.OrionClient()
    response = orionClient.get_entities()
    
    return HttpResponse(response)

def get_entity_by_id(request):

    orionClient = client.OrionClient()
    response = orionClient.get_entity_by_id(request.headers['entityID'])

    return HttpResponse(response)

def get_complete_entity_by_id(request):

    orionClient = client.OrionClient()
    response = orionClient.get_complete_entity_by_id(request.headers['entityID'])

    return HttpResponse(response)

def get_image_without_liquid(request):

    orionClient = client.OrionClient()
    response = orionClient.get_image_without_liquid()

    return HttpResponse(response)

def get_image_with_liquid(request):

    orionClient = client.OrionClient()
    response = orionClient.get_image_with_liquid()

    return HttpResponse(response)

def execute_first_protocol(request):

    orionClient = client.OrionClient()
    response = orionClient.execute_first_protocol(request.body.decode('utf-8'))

    return HttpResponse(response)

def execute_second_protocol(request):

    orionClient = client.OrionClient()
    response = orionClient.execute_second_protocol(request.body.decode('utf-8'))

    return HttpResponse(response)

def execute_third_protocol(request):

    orionClient = client.OrionClient()
    response = orionClient.execute_third_protocol(request.body.decode('utf-8'))

    return HttpResponse(response)

def execute_fourth_protocol(request):

    orionClient = client.OrionClient()
    response = orionClient.execute_fourth_protocol(request.body.decode('utf-8'))

    return HttpResponse(response)

def execute_fifth_protocol(request):

    orionClient = client.OrionClient()
    response = orionClient.execute_fifth_protocol(request.body.decode('utf-8'))

    return HttpResponse(response)







