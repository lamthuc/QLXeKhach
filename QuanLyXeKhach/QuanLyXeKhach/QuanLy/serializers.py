from rest_framework import serializers
from .models import Coach, Route

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'

# # class NhaXeSerializers(serializers.ModelSerializer):
# #     class Meta:
# #         model = NhaXe
# #         fields = ['name', 'address', 'avatar']
#
# class TuyenXeSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Route
#         fields = ['']
