from django.shortcuts import render
from master.models import Kelompok
from rest_framework import viewsets
from .serializers import Lab1Serializer, Lab2Serializer
from datetime import date

today = date.today()

class Lab1Viewset(viewsets.ModelViewSet):
  queryset = Kelompok.objects.filter(ruangan="Lab. 1", tanggal__day=today.day)
  serializer_class = Lab1Serializer

class Lab2Viewset(viewsets.ModelViewSet):
  queryset = Kelompok.objects.filter(ruangan="Lab. 2", tanggal__day=today.day)
  serializer_class = Lab2Serializer