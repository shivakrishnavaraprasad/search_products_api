from . models import Order_Detail
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Detail
        fields = '__all__'
