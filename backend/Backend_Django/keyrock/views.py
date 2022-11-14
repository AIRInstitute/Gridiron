import logging
import requests
# from backend.Backend_Django.core.clients import KeyrockClient
from rest_framework import status
from rest_framework.response import Response
import json

#Django
from django.shortcuts import render
from django.http import HttpResponse
from constance import config
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


from core import clients as client

logger = logging.getLogger(__name__)

# @csrf_exempt
def get_token(request):

    keyrockClient = client.KeyrockClient()

    # print('llego aqui')
    response = keyrockClient.get_token(f"{config.KEYROCK_HOST}:{config.KEYROCK_PORT}")
    # print('llego aqui 2')
    return HttpResponse(response)

def get_token_oauth(request):

    keyrockClient = client.KeyrockClient()

    print(f"{settings.KEYROCK_HOST}:{settings.KEYROCK_PORT}")

    # print('llego aqui')
    print(request.body)
    print(request.body.decode('utf-8'))
    response = keyrockClient.get_token_oauth(f"{settings.KEYROCK_HOST}:{settings.KEYROCK_PORT}", request.body.decode('utf-8'))
    # print('llego aqui 2')
    return HttpResponse(response)

def create_user(request):

    keyrockClient = client.KeyrockClient()

    # logging.info(request.headers['X-Auth-token'])

    # print(request.body.decode('utf-8'))

    response = keyrockClient.create_user(f"{config.KEYROCK_HOST}:{config.KEYROCK_PORT}",request.headers['X-Auth-token'], request.body.decode('utf-8'))
    
    return HttpResponse(response)


def list_users(request):

    keyrockClient = client.KeyrockClient()

    response = keyrockClient.list_users(f"{config.KEYROCK_HOST}:{config.KEYROCK_PORT}",request.headers['X-Auth-token'])

    return HttpResponse(response)


def delete_users(request):

    keyrockClient = client.KeyrockClient()

    response = keyrockClient.delete_users(f"{config.KEYROCK_HOST}:{config.KEYROCK_PORT}",request.headers['X-Auth-token'],request.headers['id-user'])

    return HttpResponse(response)


def get_user_info(request):

    keyrockClient = client.KeyrockClient()

    response = keyrockClient.get_user_info(f"{config.KEYROCK_HOST}:{config.KEYROCK_PORT}",request.headers['X-Auth-token'],request.headers['id-user'])

    return HttpResponse(response)


def update_user(request):

    keyrockClient = client.KeyrockClient()

    response = keyrockClient.update_user(f"{config.KEYROCK_HOST}:{config.KEYROCK_PORT}",request.headers['X-Auth-token'],request.headers['id-user'], request.body.decode('utf-8'))

    return HttpResponse(response)


