from ..models import Component, ComponentUsage, Calculation
from rest_framework import serializers


class ComponentSerializer(serializers.ModelSerializer):
    
    owner = serializers.StringRelatedField(read_only=True)
    system_component = serializers.BooleanField(read_only=True)

    # Define un campo DecimalField personalizado para asegurarte de que se serialice como número
    worst_case = serializers.DecimalField(max_digits=7, decimal_places=2, coerce_to_string=False)
    best_case = serializers.DecimalField(max_digits=7, decimal_places=2, coerce_to_string=False)
    middle_case = serializers.DecimalField(max_digits=7, decimal_places=2, coerce_to_string=False)
    cfp = serializers.DecimalField(max_digits=7, decimal_places=2, coerce_to_string=False)
    cfp_build_phase = serializers.DecimalField(max_digits=7, decimal_places=2, coerce_to_string=False)
    cfp_deviation_standard = serializers.DecimalField(max_digits=7, decimal_places=2, coerce_to_string=False)


    class Meta:
        model = Component
        fields = '__all__'

class ComponentUsageSerializer(serializers.ModelSerializer):
    calculation = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = ComponentUsage
        fields = '__all__' #definimos los campos que queremos transportat

class CalculationSerializer(serializers.ModelSerializer):

    owner = serializers.StringRelatedField(read_only=True)
    
    component_usage = ComponentUsageSerializer(many=True, read_only=True)
    class Meta:
        model = Calculation
        fields = '__all__' #definimos los campos que queremos transportat






 