from rest_framework import serializers
from .models import Coach, Route, BusCompany, Delivery, Review

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'

class BusCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusCompany
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    bus_company = BusCompanySerializer()

    class Meta:
        model = Route
        fields = '__all__'

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'