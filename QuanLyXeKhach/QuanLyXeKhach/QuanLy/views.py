from django.shortcuts import render
from requests import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

from .models import Coach
from .serializers import CoachSerializer
# Create your views here.
class CoachViewSet(viewsets.GenericViewSet):
     serializer_class = CoachSerializer
     queryset = Coach.objects.all()


# class NhaXeViewSet(viewsets.ModelViewSet):
#      queryset = NhaXe.objects.all()
#      serializer_class = NhaXeSerializers
#
# class TuyenXeViewSet(viewsets.ModelViewSet):
#      queryset = TuyenXe.objects.all()
#      serializer_class = TuyenXeSerializers