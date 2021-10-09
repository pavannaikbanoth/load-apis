from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from.models import *
from .serializers import *
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated


class Loadviewset(viewsets.ModelViewSet):
    queryset=Load.objects.all()
    serializer_class=LoadSerializer