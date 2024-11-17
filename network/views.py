from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from network.models import Network
from network.permissions import IsActive
from network.serializers import NetworkSerializer, NetworkUpdateSerializer


class NetworkViewSet(viewsets.ModelViewSet):
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    permission_classes = [IsActive]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('contacts__country',)

    def get_serializer_class(self):
        """Метод возвращает сериалайзер в соответствии с условием"""
        if self.action == 'update':
            return NetworkUpdateSerializer
        return NetworkSerializer
