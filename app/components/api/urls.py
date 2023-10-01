from django.urls import  path

from .viewsets import CalculationDetailAPIView, CalculationListCreateAPIView
from .viewsets import ComponentUsageDetailAPIView, ComponentUsageListCreateAPIView
from .viewsets import ComponentListCreateAPIView, ComponentDetailAPIView, SystemComponentListAPIView

urlpatterns = [
        path("component/", ComponentListCreateAPIView.as_view(), name="component-list"),
        path("component/<int:pk>/", ComponentDetailAPIView.as_view(), name="component-detail"),
        path("component/system/", SystemComponentListAPIView.as_view(), name="system-component-list"),
        
        path("calculation/", CalculationListCreateAPIView.as_view(), name="calculation-list"),
        path("calculation/<int:pk>/", CalculationDetailAPIView.as_view(), name="calculation-detail"),
        path("calculation/<int:calc_pk>/usage/", ComponentUsageListCreateAPIView.as_view(), name="usage-list"),
        
        path("usage/<int:pk>", ComponentUsageDetailAPIView.as_view(), name="usage-detail")
]