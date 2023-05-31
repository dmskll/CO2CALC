from .models import Component
from rest_framework import serializers


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__' #definimos los campos que queremos transportat
