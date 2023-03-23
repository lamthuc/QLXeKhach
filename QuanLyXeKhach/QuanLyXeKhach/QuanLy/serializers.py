from rest_framework import serializers
from .models import  ChuyenXe

class ChuyenXeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChuyenXe
        fields = ['tuyenxe', 'nhaxe']