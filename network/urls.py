from rest_framework.routers import DefaultRouter
from network.apps import ElectronicsConfig
from network.views import NetworkViewSet

app_name = ElectronicsConfig.name


router = DefaultRouter()
router.register(r'network', NetworkViewSet, basename='network')

urlpatterns = [] + router.urls
