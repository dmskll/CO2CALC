from rest_framework import routers

from .viewsets import ComponentViewSet

router = routers.SimpleRouter()
router.register(r'components', ComponentViewSet)

urlpatterns = router.urls
