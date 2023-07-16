from django.urls import include, path
from rest_framework import routers

from .viewsets import CalculationDetailAPIView, CalculationListCreateAPIView
from .viewsets import ComponentUsageDetailAPIView, ComponentUsageListCreateAPIView 
from .viewsets import ComponentListCreateAPIView, ComponentDetailAPIView, SystemComponentListAPIView

# router = routers.DefaultRouter()
# #router.register(r'components/custom/user', CustomComponentViewSet)
# router.register(r'components/custom', ComponentViewSet)
# #router.register(r'list/user/', CalculationViewSet)
# router.register(r'components', ComponentViewSet)
# # router.register(r'list', CalculationViewSet)
# router.register(r'use', ComponentUsageViewSet)

# urlpatterns = router.urls
urlpatterns = [
        path("component/", ComponentListCreateAPIView.as_view(), name="component-list"),
        path("component/<int:pk>/", ComponentDetailAPIView.as_view(), name="component-detail"),
        path("component/system/", SystemComponentListAPIView.as_view(), name="system-component-list"),
        
        path("calculation/", CalculationListCreateAPIView.as_view(), name="calculation-list"),
        path("calculation/<int:pk>/", CalculationDetailAPIView.as_view(), name="calculation-detail"),
        path("calculation/<int:calc_pk>/usage", ComponentUsageListCreateAPIView.as_view(), name="usage-list"),
        
        path("usage/<int:pk>", ComponentUsageDetailAPIView.as_view(), name="usage-detail")
]