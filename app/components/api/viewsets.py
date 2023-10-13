from rest_framework import generics
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from rest_framework.generics import get_object_or_404
from django.shortcuts import get_list_or_404
from rest_framework.exceptions import PermissionDenied

from rest_framework import permissions
from components.api.permissions import IsAdminUserOrReadOnly, IsOwner, ComponentIsOwner

from ..models import Component, ComponentUsage, Calculation
from .serializer import (
    ComponentSerializer,
    ComponentUsageSerializer,
    CalculationSerializer,
)

@swagger_auto_schema(methods=["get"])
class ComponentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Retorna el componente indicado por la id de la petición.

    put:
    Modifica el componente indicado por la id de la petición.

    delete:
    Elimina el componente indicado por la id de la petición.
    """
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    permission_classes = [ComponentIsOwner]

    @swagger_auto_schema(auto_schema=None)
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


# @method_decorator(
#     name="get",
#     decorator=swagger_auto_schema(
#         responses={
#             200: ComponentSerializer,
#             201: "buenas",
#         }
#     ),
# )
@swagger_auto_schema(methods=["get"])
class ComponentListCreateAPIView(generics.ListCreateAPIView):
    """
    get:
    Retorna los componentes creados por el usuario.

    post:
    Crea un nuevo componente.
    """

    serializer_class = ComponentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        owner = self.request.user
        system = self.request.user.is_superuser
        if not system:
            type = Component.CUSTOM

        serializer.save(owner=owner, system_component=system, type=type)

    # @swagger_auto_schema(responses={200: "buenas"})
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Component.objects.filter(owner=self.request.user)
        else:
            return Component.objects.none()


@swagger_auto_schema(methods=["get"])
class SystemComponentListAPIView(generics.ListAPIView):
    """
    get:
    Retorna los componentes de sistema, públicos para todos los usuarios.

    post:
    Crea un nuevo componente de sistema, únicamente para admin.
    """    
    queryset = Component.objects.filter(system_component=True)
    serializer_class = ComponentSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ComponentUsageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Retorna el uso indicado por la id de la petición.

    put:
    Modifica el uso indicado por la id de la petición.

    delete:
    Elimina el uso indicado por la id de la petición.
    """
    queryset = ComponentUsage.objects.all()
    serializer_class = ComponentUsageSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Component usage no tiene el atributo de owner, por eso se comprueba accediendo al owner
    # del calculo al que pertenece.
    # @swagger_auto_schema(responses={200: "buenas"})
    def get_queryset(self):
        if self.request.user.is_authenticated:
            usage_pk = self.kwargs.get("pk")
            # En este casoutilizar el get_object_or_404  genera un error producir el esquema
            # para la documentación de la api
            try:
                usage = ComponentUsage.objects.get(pk=usage_pk)
            except ComponentUsage.DoesNotExist:
                return JsonResponse(
                    {"status_code": 404, "error": "The resource was not found"}
                )

            calculation = get_object_or_404(Calculation, pk=usage.calculation.id)

            if calculation.owner != self.request.user:
                raise PermissionDenied(
                    {"detail": "You do not have permission to perform this action."}
                )

            return ComponentUsage.objects.filter(id=usage_pk)

    @swagger_auto_schema(auto_schema=None)
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


class ComponentUsageListCreateAPIView(generics.ListCreateAPIView):
    """
    get:
    Retorna los usos que pertenecen al usuario de un cálculo en concreto.

    post:
    Crea un nuevo uso en un cálculo en concreto.
    """    
    queryset = ComponentUsage.objects.all()
    serializer_class = ComponentUsageSerializer
    # permission_classes = [IsOwner]

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
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer, calc):
        serializer.save(calculation=calc)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            calc_pk = self.kwargs.get("calc_pk")
            calc = get_object_or_404(Calculation, pk=calc_pk)

            if calc.owner != self.request.user:
                raise PermissionDenied(
                    {"detail": "You do not have permission to perform this action."}
                )

            return ComponentUsage.objects.filter(calculation=calc)

        else:
            raise PermissionDenied(
                {"detail": "Authentication credentials were not provided."}
            )


class CalculationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer
    permission_classes = [IsOwner]

    @swagger_auto_schema(auto_schema=None)
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


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
        serializer.save(owner=owner)
