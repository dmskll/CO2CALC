
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import get_object_or_404
from django.shortcuts import get_list_or_404
from rest_framework.exceptions import PermissionDenied

from rest_framework import permissions
from components.api.permissions import IsAdminUserOrReadOnly, IsOwner, ComponentIsOwner

from ..models import Component, ComponentUsage, Calculation
from .serializer import ComponentSerializer, ComponentUsageSerializer, CalculationSerializer
import json


class ComponentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    permission_classes = [ComponentIsOwner]

class ComponentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ComponentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):        
        owner = self.request.user
        system = self.request.user.is_superuser
        if not system:
            type = Component.CUSTOM

        serializer.save(owner = owner, system_component = system, type = type)

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

    # Component usage no tiene el atributo de owner, por eso se comprueba accediendo al owner
    # del calculo al que pertenecjsone.
    def get_queryset(self):
        if self.request.user.is_authenticated:
            usage_pk = self.kwargs.get("pk")
            usage = get_object_or_404(ComponentUsage, pk=usage_pk) 
            calculation = get_object_or_404(Calculation, pk=usage.calculation.id)


            if calculation.owner != self.request.user:
                raise PermissionDenied({"detail":"You do not have permission to perform this action."})

            return ComponentUsage.objects.filter(id=usage_pk)
        

class ComponentUsageListCreateAPIView(generics.ListCreateAPIView):
    queryset = ComponentUsage.objects.all()
    serializer_class = ComponentUsageSerializer
    #permission_classes = [IsOwner]

    # para poder hacer el return response error, tenemos que utilizar create()
    def create(self, request, *args, **kwargs):
        calc_pk = kwargs.get("calc_pk")
        calc = get_object_or_404(Calculation, pk=calc_pk)
        
        # component = request.data.get("component")    
        # # Nos aseguramos de que no haya un  uso del mismo componente en el calculo
        # if ComponentUsage.objects.filter(component=component, calculation=calc).exists():
        #     return Response({"error": "Ya existe un uso para este componente en este cálculo."},
        #                     status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, calc)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers) 
    
    def perform_create(self, serializer, calc):        
        serializer.save(calculation = calc)
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            calc_pk = self.kwargs.get("calc_pk")
            calc = get_object_or_404(Calculation, pk=calc_pk) 
            
            if calc.owner != self.request.user:
                raise PermissionDenied({"detail":"You do not have permission to perform this action."})

            return ComponentUsage.objects.filter(calculation=calc)
        
        else:
            raise PermissionDenied({"detail":"Authentication credentials were not provided."})

    
    
class CalculationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer
    permission_classes = [IsOwner]
    
    
class CalculationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CalculationSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Calculation.objects.filter(owner=self.request.user)
        else:
            return Calculation.objects.none()
    
    def perform_create(self, serializer):        
        owner = self.request.user
        serializer.save(owner = owner)

class CalculationData(APIView):
    def get(self, request, calc_pk2):

        #calc_pk = self.kwargs.get("calc_pk2")
        user = request.user
        calc = get_object_or_404(Calculation, pk=calc_pk2)

        if calc.owner == user:
            usages = get_list_or_404(ComponentUsage, calculation=calc_pk2)
            print(usages[0].use)
            component_uses = []
            for use in usages:
                json_use = {
                    "id": use.id,
                    "calculation": use.calculation.id,
                    "hours": use.hours,
                    "use": use.use,
                    "Description": use.Description,
                    "component": use.component.id
                }
                add_component = True;
                for index, component_use in enumerate(component_uses):
                    if use.component.id == component_use["id"]:
                        component_uses[index]["usage"].append(json_use)
                        add_component = False;
                        break

                if add_component:
                    component_uses.append({
                        "id": use.component.id,
                        "owner": use.component.owner,
                        "system_component": use.component.system_component,
                        "usage": [json_use]
                    })
                    

            json_data = json.dumps(component_uses, indent=4, default=str, sort_keys=True, ensure_ascii=False)
            print(json_data)
            return Response(json_data)
        #en caso de que no esté loggeado
        return Response({
            'authenticated': False
        })
        

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


# class ComponentViewSet(viewsets.ModelViewSet):
#     queryset = Component.objects.all()
#     serializer_class = ComponentSerializer

# class ComponentViewSet(viewsets.ModelViewSet):
#     queryset = Component.objects.all()
#     serializer_class = ComponentSerializer


# class ComponentUsageViewSet(viewsets.ModelViewSet):
#     queryset = ComponentUsage.objects.all()
#     serializer_class = ComponentUsageSerializer

# class CalculationViewSet(viewsets.ModelViewSet):
#     queryset = Calculation.objects.all()
#     serializer_class = CalculationSerializer