from django.shortcuts import render
from rest_framework import viewsets
from .models import ChuyenXe
from .serializers import ChuyenXeSerializers
# Create your views here.
class ChuyenXeViewSet(viewsets.ModelViewSet):
     queryset = ChuyenXe.objects.all()
     serializer_class = ChuyenXeSerializers