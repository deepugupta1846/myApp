from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework import status
from .models import *
from .serializers import *
# Create your views here.

def Home(self):
    return HttpResponse('Hello world')
    
