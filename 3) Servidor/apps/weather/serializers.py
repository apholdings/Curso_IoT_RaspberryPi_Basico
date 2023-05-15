from rest_framework import serializers
from .models import DHT11SensorData

class DHT11SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DHT11SensorData
        fields = ['temperature', 'humidity', 'timestamp']