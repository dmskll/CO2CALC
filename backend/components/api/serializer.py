from ..models import Component, ComponentUsage, Calculation
from rest_framework import serializers


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__' #definimos los campos que queremos transportat


class ComponentUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentUsage
        fields = '__all__' #definimos los campos que queremos transportat

class CalculationSerializer(serializers.ModelSerializer):
    component_usage = ComponentUsageSerializer(many=True, read_only=True)
    class Meta:
        model = Calculation
        fields = '__all__' #definimos los campos que queremos transportat






 