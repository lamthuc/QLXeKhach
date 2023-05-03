from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers
from . import views

r = routers.DefaultRouter()
r.register('coach', views.CoachSerializer, basename='coach')

# r.register('tuyenxe', views.TuyenXeSerializers, basename='TuyenXe')
# r.register('nhaxe', views.NhaXeSerializers, basename='NhaXe')

urlpatterns = [
    path('/', include(r.urls)),
]