
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from ..models import Component, ComponentUsage, Calculation
from .serializer import ComponentSerializer, ComponentUsageSerializer, CalculationSerializer

class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer


class ComponentUsageViewSet(viewsets.ModelViewSet):
    queryset = ComponentUsage.objects.all()
    serializer_class = ComponentUsageSerializer

# class CalculationViewSet(viewsets.ModelViewSet):
#     queryset = Calculation.objects.all()
#     serializer_class = CalculationSerializer


class ComponentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class ComponentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class SystemComponentListAPIView(generics.ListAPIView):
    queryset = Component.objects.filter(system_component=True)
    serializer_class = ComponentSerializer


class ComponentUsageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComponentUsage.objects.all()
    serializer_class = ComponentUsageSerializer

class ComponentUsageListCreateAPIView(generics.ListCreateAPIView):
    queryset = ComponentUsage.objects.all()
    serializer_class = ComponentUsageSerializer

    def perform_create(self, serializer):
        calc_pk = self.kwargs.get("calc_pk")
        calc    = get_object_or_404(Calculation, pk=calc_pk)
        serializer.save(calculation=calc)
        
class CalculationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer

class CalculationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer


# class CalculationViewSet(APIView):
    
#     def get(self, request):
#         component_list = Calculation.objects.all()
#         serializer = CalculationSerializer(component_list, 
#                                           many=True)
#         return Response(serializer.data)      

#     def post(self, request):
#         serializer = CalculationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  