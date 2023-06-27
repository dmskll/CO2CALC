
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Component, ComponentUsage, ComponentList
from .serializer import ComponentSerializer, ComponentUsageSerializer, ComponentListSerializer

class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer


class ComponentUsageViewSet(viewsets.ModelViewSet):
    queryset = ComponentUsage.objects.all()
    serializer_class = ComponentUsageSerializer

# class ComponentListViewSet(viewsets.ModelViewSet):
#     queryset = ComponentList.objects.all()
#     serializer_class = ComponentListSerializer

class ComponentListViewSet(APIView):
    
    def get(self, request):
        component_list = ComponentList.objects.all()
        serializer = ComponentListSerializer(component_list, 
                                          many=True)
        return Response(serializer.data)      

    def post(self, request):
        serializer = ComponentListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  