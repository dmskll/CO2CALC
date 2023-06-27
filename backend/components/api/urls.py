from django.urls import include, path
from rest_framework import routers

from .viewsets import ComponentViewSet, ComponentListViewSet, ComponentUsageViewSet

router = routers.DefaultRouter()
#router.register(r'components/custom/user', CustomComponentViewSet)
router.register(r'components/custom', ComponentViewSet)
#router.register(r'list/user/', ComponentListViewSet)
router.register(r'components', ComponentViewSet)
# router.register(r'list', ComponentListViewSet)
router.register(r'use', ComponentUsageViewSet)

urlpatterns = router.urls
urlpatterns += [
        path("journalists/", 
         ComponentListViewSet.as_view(), 
         name="ComponentList-list")
]