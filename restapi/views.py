from django.core import serializers
from django.forms import forms
from django.http import QueryDict
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from rest_framework import request
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.parsers import MultiPartParser
import json
from restapi.models import User
from restapi.serialize import UserSerializer
from restapi.userencoder import UserEncoder


@api_view(http_method_names=['GET'])
@parser_classes((JSONParser, MultiPartParser,))
@permission_classes((permissions.AllowAny,))
def getUserList(request):
    print "!!!!!!!!!!!!!!!"
    print request.query_params.get('username',None)
    #list = User.objects.all()
    es = User.objects.all()
    for e in es:
        print(e.username)

    return Response([
        {"name": "admin", "password": "123"},
        {"name": "list", "password": "456"},
    ])


@api_view(http_method_names=['POST'])
@parser_classes((JSONParser, FormParser, MultiPartParser))
@permission_classes((permissions.AllowAny,))
def login(request):
    #raw: [{"username": "admin", "password" : "12345"}]
    #print "----login-----"
    data = json.loads(request.body)
    #print data
    username = data[0]['username']
    password = data[0]['password']
    #print username
    #print password

    querySet = User.objects.filter(username__exact = username, password__exact = password)

    if any(querySet):
        for e in querySet:
            user = User(id=e.id, username=e.username, password=e.password, age=e.age, sex=e.sex, email=e.email)
            user.save()
            # print user
            # print UserEncoder().encode(user)
            userStr = json.dumps(user, cls= UserEncoder)
            # print userStr

        return Response({
            "data": userStr
        },status=status.HTTP_202_ACCEPTED)
    else:
        return Response({
            "data": ""
        },status=status.HTTP_404_NOT_FOUND)


@api_view(http_method_names=['POST'])
@parser_classes((JSONParser, FormParser, MultiPartParser))
@permission_classes((permissions.AllowAny,))
def modifyEmail(request):
    data = json.loads(request.body)
    id = data[0]['id']
    email = data[0]['email']
    user = User.objects.get(id=id)
    user.email = email
    user.save()
    userStr = json.dumps(user, cls=UserEncoder)
    return Response({
        "data": userStr
    }, status=status.HTTP_202_ACCEPTED)




