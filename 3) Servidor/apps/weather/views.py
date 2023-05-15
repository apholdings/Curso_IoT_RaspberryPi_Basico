from rest_framework_api.views import StandardAPIView
from rest_framework import status, permissions
from .models import DHT11SensorData
from .serializers import DHT11SensorDataSerializer
from .mqtt import publish


# Create, List
class ListDHT11SensorData(StandardAPIView):
    def get(self, request, *args, **kwargs):
        sensor_data = DHT11SensorData.objects.all()
        serializer = DHT11SensorDataSerializer(sensor_data, many=True)
        return self.paginate_response(request, serializer.data)
    

class AddDHT11SensorData(StandardAPIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):

        data = self.request.data
        humidity = data['humidity']
        temperature = data['temperature']
        
        if humidity is not None and temperature is not None:
            new_data = DHT11SensorData.objects.create(humidity=humidity, temperature=temperature)
            serializer = DHT11SensorDataSerializer(new_data)
            return self.send_response(serializer.data)
        else:
            return self.send_error("Failed to read from sensor")

class ToggleLEDView(StandardAPIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        publish("led/control","off")
        return self.send_response("LED Turned ON")    