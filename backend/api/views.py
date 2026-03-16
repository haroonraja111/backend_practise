from django.http import response
from django.shortcuts import render
from requests import api
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime


# Create your views here.
@api_view(['GET'])
def health_check(request):
    return Response({
        'status' : 'healthy',
        'time' : datetime.now().isoformat()
    })



@api_view(['GET'])
def hello_world(request):
    return Response({'messages' : 'Hallo world...'})