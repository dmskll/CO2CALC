
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from rest_framework import permissions
from components.api.permissions import IsAdminUserOrReadOnly, IsOwner

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
    permission_classes = [IsOwner]

class ComponentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ComponentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):        
        owner = self.request.user
        system = self.request.user.is_superuser
        serializer.save(owner = owner, system_component = system)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Component.objects.filter(owner=self.request.user)
        else:
            return Component.objects.none()


class SystemComponentListAPIView(generics.ListAPIView):
    queryset = Component.objects.filter(system_component=True)
    serializer_class = ComponentSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ComponentUsageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComponentUsage.objects.all()
    serializer_class = ComponentUsageSerializer
    permission_classes = [permissions.IsAuthenticated]

    #user

class ComponentUsageListCreateAPIView(generics.ListCreateAPIView):
    queryset = ComponentUsage.objects.all()
    serializer_class = ComponentUsageSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        calc_pk = self.kwargs.get("calc_pk")
        calc = get_object_or_404(Calculation, pk=calc_pk)
        
        owner = self.request.user
        
        serializer.save(calculation=calc, owner = owner)
    #user
    
class CalculationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer
    permission_classes = [IsOwner]
    

class CalculationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer
    permission_classes = [IsOwner]

    

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