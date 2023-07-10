from ..models import Component, ComponentUsage, Calculation
from rest_framework import serializers


class ComponentSerializer(serializers.ModelSerializer):
    
    owner = serializers.StringRelatedField(read_only=True)
    system_component = serializers.BooleanField(read_only=True)

    class Meta:
        model = Component
        fields = '__all__'

class ComponentUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentUsage
        fields = '__all__' #definimos los campos que queremos transportat

class CalculationSerializer(serializers.ModelSerializer):

    owner = serializers.StringRelatedField(read_only=True)
    
    component_usage = ComponentUsageSerializer(many=True, read_only=True)
    class Meta:
        model = Calculation
        fields = '__all__' #definimos los campos que queremos transportat






 