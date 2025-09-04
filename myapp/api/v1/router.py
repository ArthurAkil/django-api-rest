from rest_framework.routers import DefaultRouter
from .viewsets import ClientViewSet, ProductViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)


urlpatterns = router.urls