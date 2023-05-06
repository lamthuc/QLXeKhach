from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers
from .views import RouteSearchView, RecommendedRoutesView, CoachSerializer, RegisterBusCompanyView, BusCompanyUpdateView, BusCompanyDetailView,BusCompanyRoutesView, BusCompanyCoachView, BusCompanyCreateRouteView, BusCompanyUpdateRouteView

r = routers.DefaultRouter()
# r.register('coach', views.CoachSerializer, basename='coach')

# r.register('tuyenxe', views.TuyenXeSerializers, basename='TuyenXe')
# r.register('nhaxe', views.NhaXeSerializers, basename='NhaXe')

urlpatterns = [
    path('register/', RegisterBusCompanyView.as_view(), name='transport-company-register'),
    # Cập nhật thông tin nhà xe
    path('update/<int:pk>/', BusCompanyUpdateView.as_view(), name='transport-company-update'),
    # Lấy thông tin nhà xe
    path('detail/<int:pk>/', BusCompanyDetailView.as_view(), name='transport-company-detail'),
    # Lấy danh sách các tuyến xe của nhà xe
    path('<int:pk>/routes/', BusCompanyRoutesView.as_view(), name='transport-company-routes'),
    # Lấy danh sách các chuyến xe của nhà xe
    path('<int:pk>/trips/', BusCompanyCoachView.as_view(), name='transport-company-coach'),
    # Tạo mới tuyến xe cho nhà xe
    path('<int:pk>/routes/create/', BusCompanyCreateRouteView.as_view(), name='transport-company-create-route'),
    # Tạo mới chuyến xe cho nhà xe
    # path('<int:pk>/trips/create/', BusCompanyCreateTripView.as_view(), name='transport-company-create-trip'),
    # Cập nhật tuyến xe của nhà xe
    path('routes/update/<int:pk>/', BusCompanyUpdateRouteView.as_view(), name='transport-company-update-route'),
    # Cập nhật chuyến xe của nhà xe
    # path('trips/update/<int:pk>/', BusCompanyUpdateTripView.as_view(), name='transport-company-update-trip'),
    path('routes/search/', RouteSearchView.as_view(), name='route_search'),
    path('routes/recommended/', RecommendedRoutesView.as_view(), name='recommended_routes'),
    path('/', include(r.urls)),

]
