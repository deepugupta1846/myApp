from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework import status
from .models import *
from .serializers import *
# Create your views here.

class ReadOnlyView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

class CompanyViews(ReadOnlyView):
    def get(self, request):
        queryset = Company.objects.all()
        return Response({'data': queryset})
    
