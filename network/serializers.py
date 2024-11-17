from rest_framework import serializers
from network.models import Network


class NetworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Network
        fields = '__all__'


class NetworkUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Network
        fields = '__all__'
        read_only_fields = ['arrears']
