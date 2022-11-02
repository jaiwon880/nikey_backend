from django.shortcuts import render
from rest_framework import viewsets # viewset import
from .serializer import UserSerializer # 생성한 serializer import
from .models import User # User model import

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        query_set = User.objects.all()
        serializer = UserSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt # 단건 조회
def user(request, pk):
    obj = User.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = UserSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_name = data['name']
        obj = User.objects.get(name=search_name)

        if data['phone_number'] == obj.phone_number:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)